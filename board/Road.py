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


Player = TypeVar("Player")
Road = TypeVar("Road")
Settlement = TypeVar("Settlement")
Tile = TypeVar("Tile")


class Road:
	class Settlements(Enum):
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
		LEFT: int
		RIGHT: int


	class Tiles(Enum):
		r"""
		Below are depictions of tiles relative to settlements.

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
		BOTTOM: int
		TOP: int


	def __init__(self, id: int):
		self.id: int = id
		# Board parts
		self.settlements: list[Settlement] = [None, None]
		self.tiles: list[Tile] = [None, None]
		# Game state
		self.player: Optional[Player] = None  # The player who owns the road if any.


	def __eq__(self, right: Settlement) -> bool:
		return self.id == right.id


	def __iter__(self) -> iter:
		yield from {
			"id": self.id,
			"Settlements": {
				f"Tile::Settlements::{self.Settlements.ENUM_KEYS[index]}": settlement.id
				for index, settlement in enumerate(self.settlements)
				if(settlement)
			},
			"Tiles": {
				f"Settlement::Tiles::{self.Tiles.ENUM_KEYS[index]}": tile.id
				for index, tile in enumerate(self.tiles)
				if(tile)
			}
		}.items()
