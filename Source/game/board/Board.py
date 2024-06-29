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
from typing import Optional, Tuple


from game.board import Port
from game.board import Road
from game.board import Robber
from game.board import Settlement
from game.board import Tile


class Board:
	def __init__(self, id: int, size: Tuple[int, int], ports: Optional[list[Port]]=None,
		roads: Optional[list[Road]]=None, robber: Optional[Robber]=None, settlements: Optional[list[Settlement]]=None,
		tiles: Optional[list[Tile]]=None
	):
		self.id: int = id
		self.size: int = size
		self.ports: list[Port] = list(ports) if(ports is not None) else []
		self.robber: Robber = robber
		self.roads: list[Road] = list(roads) if(roads is not None) else []
		self.settlements: list[Settlement] = list(settlements) if(settlements is not None) else []
		self.tiles: list[Tile] = list(tiles) if(tiles is not None) else []


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"size": self.size,
			"ports": list(map(dict, self.ports)),
			"robber": dict(self.robber),
			"roads": list(map(dict, self.roads)),
			"settlements": list(map(dict, self.settlements)),
			"tiles": list(map(dict, self.tiles)),
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4)
