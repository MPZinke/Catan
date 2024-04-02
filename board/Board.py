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


from board import Border
from board import Corner
from board import Tile


class Board:
	def __init__(self, borders: Optional[list[Border]]=None, corners: Optional[list[Corner]]=None,
		tiles: Optional[list[Tile]]=None
	):
		self.borders: list[Border] = list(borders) if(borders is not None) else []
		self.corners: list[Corner] = list(corners) if(corners is not None) else []
		self.tiles: list[Tile] = list(tiles) if(tiles is not None) else []
