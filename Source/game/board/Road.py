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
from database.queries import directions


Player = TypeVar("Player")
Road = TypeVar("Road")
Roads = list[Optional[Road]]
Settlement = TypeVar("Settlement")
Settlements = list[Optional[Settlement]]
Tile = TypeVar("Tile")
Tiles = list[Optional[Tile]]


class Road:
	Settlements = Enum("Road::Settlements", **{type["label"]: type["id"]-1 for type in directions.get_edge_corners()})
	r"""
	Given Figure 1 for the tile and its settlements,
	      1_________2   
	      /.........\   
	     /...........\  
	   6/.............\3
	    \............./ 
	     \.........../  
	      \_________/   
	      5         4   

	For the line 1–2 settlement 1 is left and 2 right, while for line 4–5, 4 is right and 5 is left.
	    1_________2           \.........../  
	    /.........\            \_________/   
	   /...........\           5         4   

	For the line 1–6 settlement 1 is right and 6 left, while for line 3–4, 3 is right and 4 is left.
	      1_____          .......\3
	      /.....          ......./ 
	     /......          ....../  
	   6/.......          _____/   
	    \.......               4   

	For the line 2–3 settlement 2 is left and 3 right, while for line 5–6, 5 is right and 6 is left.
	   _____2             6/.......
	   .....\              \.......
	   ......\              \......
	   .......\3             \_____
	   ......./              5     
	"""

	Tiles = Enum("Road::Tiles", **{type["label"]: type["id"]-1 for type in directions.get_edge_sides()})
	r"""
	Below are depictions of tiles relative to roads.

	   \.....TOP...../
	    \.........../
	     \_________/ 
	     /~~~~~~~~~\ 
	    /~~BOTTOM~~~\
	   /~~~~~~~~~~~~~\ 

	   ......\
	   .......\______
	   ..TOP../~~~~~~
	   ....../~~~~~~~
	   _____/~~BOTTOM
	        \~~~~~~~~
	         \~~~~~~~

	          /......
	   ______/.......
	   ~~~~~~\..TOP..
	   ~~~~~~~\......
	   BOTTOM~~\_____
	   ~~~~~~~~/     
	   ~~~~~~~/
	"""


	def __init__(self, id: int):
		self.id: int = id
		# Board parts
		self.settlements: Settlements = [None for _ in range(self.Settlements.length)]
		self.tiles: Tiles = [None for _ in range(self.Tiles.length)]
		# Game state
		self.player: Optional[Player] = None  # The player who owns the road if any.


	def __eq__(self, right: Settlement) -> bool:
		if(right is None):
			return False

		return self.id == right.id


	# def __iter__(self) -> iter:
	# 	yield from {
	# 		"id": self.id,
	# 		"TemplatesSettlements": {
	# 			f"Tile::Settlements::{self.Settlements.ENUM_KEYS[index]}": settlement.id
	# 			for index, settlement in enumerate(self.settlements)
	# 			if(settlement)
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

	# 	settlement_left = self.settlements[self.Settlements.LEFT]
	# 	settlement_right = self.settlements[self.Settlements.RIGHT]
	# 	tile_bottom = self.tiles[self.Tiles.BOTTOM]
	# 	tile_top = self.tiles[self.Tiles.TOP]

	# 	_id = self.id
	# 	s_l = center(settlement_left.id if(settlement_left) else "-")
	# 	s_r = center(settlement_right.id if(settlement_right) else "-")
	# 	t_b = center(tile_bottom.id if(tile_bottom) else "-")
	# 	t_t = center(tile_top.id if(tile_top) else "-")

	# 	if(
	# 		(tile_bottom and tile_bottom.roads[Tile.Roads.TOP_RIGHT].id == self.id)
	# 		or (tile_top and tile_top.roads[Tile.Roads.BOTTOM_LEFT].id == self.id)
	# 	):
	# 		return (
	# 			r" {a}/        " "\n"
	# 			r"    \     {b}" "\n"
	# 			r"     {c}     " "\n"
	# 			r"{d}   \______" "\n"
	# 			r"      /{e}   " "\n"
	# 		).format(a=s_l, b=t_t, c=_id, d=t_b, e=s_r)
	# 	if(
	# 		(tile_bottom and tile_bottom.roads[Tile.Roads.TOP_LEFT].id == self.id)
	# 		or (tile_top and tile_top.roads[Tile.Roads.BOTTOM_RIGHT].id == self.id)
	# 	):
	# 		return (
	# 			r"      \{a}   " "\n"
	# 			r"{b}   /      " "\n"
	# 			r"     {c}     " "\n"
	# 			r"____/     {d}" "\n"
	# 			r" {e}\        " "\n"
	# 		).format(a=s_r, b=t_t, c=_id, d=t_b, e=s_l)
	# 	return (
	# 		r" \    {a}    / " "\n"
	# 		r"  \         /  " "\n"
	# 		r"{b}---{c}---{d}" "\n"
	# 		r"  /         \  " "\n"
	# 		r" /    {e}    \ " "\n"
	# 	).format(a=t_t, b=s_l, c=_id, d=s_r, e=t_b)


	# def __repr__(self) -> str:
	# 	return str(self)


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"player": self.player.id if(self.player) else None,
			"settlements": [settlement.id if(settlement) else None for settlement in self.settlements],
			"tiles": [tile.id if(tile) else None for tile in self.tiles],
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4)
