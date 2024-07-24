#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.07.23                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import json
from typing import Optional, Tuple, TypeVar


from database import queries


PlayerColor = TypeVar("PlayerColor")
LobbyPlayer = TypeVar("LobbyPlayer")


class PlayerColor:
	def __init__(self, id: int, label: str, rgb: Tuple[int, int, int], hex: str):
		self.id: int = id
		self.label: str = label
		self.red: int = rgb[0]
		self.green: int = rgb[1]
		self.blue: int = rgb[2]
		self.hex: str = hex


	@property
	def rgb(self) -> Tuple[int, int, int]:
		return [self.red, self.green, self.blue]


	def __iter__(self) -> list[int]:
		yield from [self.red, self.green, self.blue]


_player_color_dicts: list[dict] = queries.player_colors.get_player_colors()
PLAYER_COLORS: list[PlayerColor] = [PlayerColor(**color_dict) for color_dict in _player_color_dicts]
