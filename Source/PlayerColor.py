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
		self.rgb: Tuple[int, int, int] = list(rgb)
		self.hex: str = hex


	def __eq__(self, right: int | str | PlayerColor) -> bool:
		if(isinstance(right, PlayerColor)):
			return self.id == right.id

		if(isinstance(right, str)):
			return self.label == right

		if(isinstance(right, int)):
			return self.id == right

		raise TypeError(f"PlayerColor.__eq__ expects type int | str | PlayerColor, not {type(right).__name__}")


	@property
	def rgb(self) -> Tuple[int, int, int]:
		return [self._rgb[0], self._rgb[1], self._rgb[2]]


	@rgb.setter
	def rgb(self, rgb: Tuple[int, int, int]) -> None:
		self._rgb = list(rgb)


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"label": self.label,
			"rgb": self.rgb,
			"hex": self.hex
		}.items()


_player_color_dicts: list[dict] = queries.player_colors.get_player_colors()
PLAYER_COLORS: list[PlayerColor] = [PlayerColor(**color_dict) for color_dict in _player_color_dicts]
