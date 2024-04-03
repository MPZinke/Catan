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


from typing import TypeVar


from Enum import Enum


Border = TypeVar("Border")
Corner = TypeVar("Corner")
Tile = TypeVar("Tile")


class Border:
	class Corners(Enum):
		"""
		Corners relative to edges
		 Edges
		  4  3  2
		   \ | / 
		     ⬣
		   / | \
		  5  0  1

		 0, 3.
		  LEFT————RIGHT

		 1, 4.
		      RIGHT
		      /
		     /
		  LEFT

		 2, 5.
		  LEFT
		   \
		    \
		    RIGHT
		"""
		LEFT: int
		RIGHT: int


	class Tiles(Enum):
		"""
		Tile relative to edge
		 Edges
		  4  3  2
		   \ | / 
		     ⬣
		   / | \
		  5  0  1

		 0, 3.
		   TOP
		  ——————
		  BOTTOM

		 1, 4.
		  TOP /
		     / BOTTOM

		 2, 5.
		        \ TOP
		  BOTTOM \
		"""
		BOTTOM: int
		TOP: int


	def __init__(self, id: int):
		self.id: int = id
		self.corners: list[Corner] = [None, None]
		self.tiles: list[Tile] = [None, None]


	def __iter__(self) -> iter:
		yield from {
			"id": self.id,
			"Corners": {
				f"Tile::Corners::{self.Corners.ENUM_KEYS[index]}": corner.id
				for index, corner in enumerate(self.corners)
				if(corner)
			},
			"Tiles": {
				f"Corner::Tiles::{self.Tiles.ENUM_KEYS[index]}": tile.id
				for index, tile in enumerate(self.tiles)
				if(tile)
			}
		}.items()
