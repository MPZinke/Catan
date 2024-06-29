#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.05.12                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import json
from typing import Optional


from game.board import Tile


class Robber:
	def __init__(self, id: int, is_friendly: bool):
		self.id: int = id
		self.is_friendly: bool = is_friendly
		self.tile: Optional[Tile] = None


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"is_friendly": self.is_friendly,
			"tile": self.tile.id if(self.tile) else None,
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4)

