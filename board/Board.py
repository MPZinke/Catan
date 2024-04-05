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


from board import Road
from board import Settlement
from board import Tile


class Board:
	def __init__(self, roads: Optional[list[Road]]=None, settlements: Optional[list[Settlement]]=None,
		tiles: Optional[list[Tile]]=None
	):
		self.roads: list[Road] = list(roads) if(roads is not None) else []
		self.settlements: list[Settlement] = list(settlements) if(settlements is not None) else []
		self.tiles: list[Tile] = list(tiles) if(tiles is not None) else []
