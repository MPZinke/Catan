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


from typing import Optional, TypeVar


from Enum import Enum


Road = TypeVar("Road")
Settlement = TypeVar("Settlement")
Tile = TypeVar("Tile")

Player = TypeVar("Player")
Port = TypeVar("Port")


class Settlement:
	class Ports(Enum):
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
		TOP: int
		BOTTOM: int
		SIDE: int


	class Roads(Enum):
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
		BOTTOM: int
		TOP: int
		SIDE: int


	class Tiles(Enum):
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
		BOTTOM: int
		TOP: int
		SIDE: int


	class Types(Enum):
		UNENHABITED: int
		VILLAGE: int
		CITY: int


	def __init__(self, id: int, type: int=Types.UNENHABITED):
		self.id: int = id

		# Board parts
		self.ports: list[Port] = [None, None, None]
		self.roads: list[Road] = [None, None, None]
		self.tiles: list[Tile] = [None, None, None]

		# Game state
		self.player: Optional[Player] = None
		self.type: int = type


	def __eq__(self, right: Settlement) -> bool:
		return self.id == right.id


	def __iter__(self) -> iter:
		yield from {
			"id": self.id,
			"Roads": {
				f"Tile::Roads::{self.Roads.ENUM_KEYS[index]}": road.id
				for index, road in enumerate(self.roads) if(road)
			},
			"Tiles": {
				f"Settlement::Tiles::{self.Tiles.ENUM_KEYS[index]}": tile.id
				for index, tile in enumerate(self.tiles)
				if(tile)
			}
		}.items()
