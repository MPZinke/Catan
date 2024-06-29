#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.01                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import json
from typing import Optional, TypeVar


from Enum import Enum
from database.queries import directions, types


Port = TypeVar("Port")
Ports = list[Optional[Port]]
Road = TypeVar("Road")
Roads = list[Optional[Road]]
Settlement = TypeVar("Settlement")
Settlements = list[Optional[Settlement]]
Tile = TypeVar("Tile")
Tiles = list[Optional[Tile]]

Player = TypeVar("Player")


class Settlement:
	Ports = Enum("Settlement::Ports", **{type["label"]: type["id"]-1 for type in directions.get_corner_sides()})
	r"""
	Given Figure 1 for the tile and its settlements,

	Figure 1.
	     1_________2   
	     /.........\   
	    /...........\  
	  6/.............\3
	   \ ........... / 
	    \ ......... /  
	     \_________/   
	     5         4


	Figure 2's shows left ports for settlements 1, 5, & 6.

	Figure 2.
	  P______1______
	   \    /.......
	    \  /........
	    6\/.........
	     /\.........
	    /  \........
	   /____\_______
	  P     5   


	Figure 3 & 4 show left ports for 2 & 4 and right ports for 1 & 5.

	Figure 3.          Figure 4.
	        P             \.........../
	       / \             \........./
	      /   \            5\‾‾‾‾‾‾‾/4
	     /     \             \     /
	   1/_______\2            \   /
	   /.........\             \ /
	  /...........\             P
	                      

	Figure 5 shows right ports for 2, 3, & 4.

	Figure 5.
	   ______2______
	   .......\    /
	   ........\  /
	   .........\/3
	   ........./\
	   ......../  \
	   _______/____\
	      4   
	"""

	Roads = Enum("Settlement::Roads", **{type["label"]: type["id"]-1 for type in directions.get_corner_edges()})
	r"""
	Below are depictions of roads relative to settlements with the following labeling:
	- 1: TOP
	- 2: SIDE
	- 3: BOTTOM
	  _____/.............\
	  ~~~~~\............./
	  ~~~~~~1.........../
	  ~~~~~~~\___2_____/
	  ~~~~~~~/°°°°°°°°°\
	  ~~~~~~3°°°°°°°°°°°\
	  _____/°°°°°°°°°°°°°\
	       \°°°°°°°°°°°°°/

	  /.............\_____
	  \............./~~~~~
	   \...........1~~~~~~
	    \_____2___/~~~~~~~
	    /°°°°°°°°°\~~~~~~~
	   /°°°°°°°°°°°3~~~~~~
	  /°°°°°°°°°°°°°\_____
	  \°°°°°°°°°°°°°/
	"""

	Tiles = Enum("Settlement::Tiles", **{type["label"]: type["id"]-1 for type in directions.get_corner_sides()})
	r"""
	Below are depictions of tiles relative to settlements.
	  _____/.............\
	  ~~~~~\.....TOP...../
	  ~~~~~~\.........../
	  ~SIDE~~\_________/
	  ~~~~~~~/°°°°°°°°°\
	  ~~~~~~/°°BOTTOM°°°\
	  _____/°°°°°°°°°°°°°\
	       \°°°°°°°°°°°°°/

	  /.............\_____
	  \.....TOP...../~~~~~
	   \.........../~~~~~~
	    \_________/~SIDE~~
	    /°°°°°°°°°\~~~~~~~
	   /°°BOTTOM°°°\~~~~~~
	  /°°°°°°°°°°°°°\_____
	  \°°°°°°°°°°°°°/
	"""

	Types = Enum("Settlement::Types", **{type["label"]: type["id"]-1 for type in types.get_settlement_types()})


	def __init__(self, id: int, type: int=Types.UNENHABITED):
		self.id: int = id

		# Board parts
		self.ports: Port = [None for _ in range(self.Ports.length)]
		self.roads: Road = [None for _ in range(self.Roads.length)]
		self.tiles: Tile = [None for _ in range(self.Tiles.length)]

		# Game state
		self.player: Optional[Player] = None
		self.type: int = type


	def __eq__(self, right: Settlement) -> bool:
		return self.id == right.id


	# def __iter__(self) -> iter:
	# 	yield from {
	# 		"id": self.id,
	# 		"TemplatesRoads": {
	# 			f"Tile::Roads::{self.Roads.ENUM_KEYS[index]}": road.id
	# 			for index, road in enumerate(self.roads) if(road)
	# 		},
	# 		"TemplatesTiles": {
	# 			f"Settlement::Tiles::{self.Tiles.ENUM_KEYS[index]}": tile.id
	# 			for index, tile in enumerate(self.tiles)
	# 			if(tile)
	# 		}
	# 	}.items()


	# def __str__(self) -> str:
	# 	from game.board import Tile

	# 	def center(value: int, space_length: int=3, padder: str=' ') -> str:
	# 		value_string: str = str(value)
	# 		value_length: int = len(value_string)

	# 		if(value_length >= space_length):
	# 			return value_string

	# 		else:
	# 			length_difference: int = space_length - value_length
	# 			side_padding_length: int = length_difference // 2
	# 			additional_padding: int = length_difference - (side_padding_length * 2)

	# 			side_padding: str = padder * side_padding_length
	# 			return f"""{side_padding}{value_string}{padder * additional_padding}{side_padding}"""

	# 	road_bottom = self.roads[self.Roads.BOTTOM]
	# 	road_side = self.roads[self.Roads.SIDE]
	# 	road_top = self.roads[self.Roads.TOP]
	# 	tile_bottom = self.tiles[self.Tiles.BOTTOM]
	# 	tile_side = self.tiles[self.Tiles.SIDE]
	# 	tile_top = self.tiles[self.Tiles.TOP]

	# 	_id = self.id
	# 	r_b = center(road_bottom.id if(road_bottom) else "-")
	# 	r_s = center(road_side.id if(road_side) else "-")
	# 	r_t = center(road_top.id if(road_top) else "-")
	# 	t_b = center(tile_bottom.id if(tile_bottom) else "-")
	# 	t_s = center(tile_side.id if(tile_side) else "-")
	# 	t_t = center(tile_top.id if(tile_top) else "-")

	# 	if(
	# 		(tile_bottom and tile_bottom.settlements[Tile.Settlements.TOP_LEFT].id == self.id)
	# 		or (tile_top and tile_top.settlements[Tile.Settlements.BOTTOM_LEFT].id == self.id)
	# 		or (tile_side and tile_side.settlements[Tile.Settlements.LEFT].id == self.id)
	# 	):
	# 		return (
	# 			r"    \      {a}  " "\n"
	# 			r"    {b}         " "\n"
	# 			r"      \         " "\n"
	# 			r"{c}    {d}---{e}" "\n"
	# 			r"      /         " "\n"
	# 			r"    {f}         " "\n"
	# 			r"    /      {g}  " "\n"
	# 		).format(a=t_t, b=r_t, c=t_s, d=_id, e=r_s, f=r_b, g=t_b)
	# 	return (
	# 		r" {a}      /     " "\n"
	# 		r"        {b}     " "\n"
	# 		r"        /       " "\n"
	# 		r"{c}---{d}    {e}" "\n"
	# 		r"        \       " "\n"
	# 		r"        {f}     " "\n"
	# 		r" {g}      \     " "\n"
	# 	).format(a=t_t, b=r_t, c=r_s, d=_id, e=t_s, f=r_b, g=t_b)


	# def __repr__(self) -> str:
	# 	return str(self)


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"type": self.type,
			"player": self.player.id if(self.player) else None,
			"ports": [port.id if(port) else None for port in self.ports],
			"roads": [road.id if(road) else None for road in self.roads],
			"tiles": [tile.id if(tile) else None for tile in self.tiles],
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4)
