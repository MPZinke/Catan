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


from typing import Optional


from game.board import Port
from game.board import Road
from game.board import Robber
from game.board import Settlement
from game.board import Tile


class Board:
	def __init__(self, ports: Optional[list[Port]], roads: Optional[list[Road]]=None, robber: Optional[Robber]=None,
		settlements: Optional[list[Settlement]]=None, tiles: Optional[list[Tile]]=None
	):
		self.ports: list[Port] = list(ports) if(ports is not None) else []
		self.robber: Robber = robber
		self.roads: list[Road] = list(roads) if(roads is not None) else []
		self.settlements: list[Settlement] = list(settlements) if(settlements is not None) else []
		self.tiles: list[Tile] = list(tiles) if(tiles is not None) else []
