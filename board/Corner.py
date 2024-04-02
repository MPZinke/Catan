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


class Corner:
	class Borders(Enum):
		"""
		Edges relative to corner
		 TOP
		   \__ SIDE
		   /
		 BOTTOM

		        TOP
		 SIDE __/
		        \
		        BOTTOM
		"""
		BOTTOM: int
		TOP: int
		SIDE: int


	class Tiles(Enum):
		"""
		Tiles relative to corners
		          ______
		         /      \
		  ______/        \
		 /      \  TOP   /
		/  SIDE  \______/
		\        /      \
		 \______/ BOTTOM \
		        \        /
		         \______/
		  ______
		 /      \
		/        \______
		\   TOP  /      \
		 \______/  SIDE  \
		 /      \        /
		/ BOTTOM \______/
		\        /
		 \______/
		"""
		BOTTOM: int
		TOP: int
		SIDE: int


	def __init__(self, id: int):
		self.id: int = id
		self.borders: list[Border] = [None, None, None]
		self.tiles: list[Tile] = [None, None, None]


	def __iter__(self) -> iter:
		yield from {
			"id": self.id,
			"Borders": {
				f"Tile::Borders::{self.Borders.ENUM_KEYS[index]}": border.id
				for index, border in enumerate(self.borders)
				if(border)
			},
			"Tiles": {
				f"Corner::Tiles::{self.Tiles.ENUM_KEYS[index]}": tile.id
				for index, tile in enumerate(self.tiles)
				if(tile)
			}
		}.items()
