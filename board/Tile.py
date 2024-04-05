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


from typing import Tuple, TypeVar


from Enum import Enum
from ResourceType import ResourceType


Road = TypeVar("Road")
Settlement = TypeVar("Settlement")
Tile = TypeVar("Tile")


class Tile:
	class Roads(Enum):
		r"""
		Roads relative to hexagon
		 Roads
		  4  3  2
		   \ | / 
		     ⬣
		   / | \
		  5  0  1
		"""
		BOTTOM: int
		BOTTOM_RIGHT: int
		TOP_RIGHT: int
		TOP: int
		TOP_LEFT: int
		BOTTOM_LEFT: int


	class Settlements(Enum):
		r"""
		Settlements relative to hexagon
		   4    3
		    \  / 
		 5 — ⬣ — 2
		    /  \
		   0    1
		"""
		BOTTOM_LEFT: int
		BOTTOM_RIGHT: int
		RIGHT: int
		TOP_RIGHT: int
		TOP_LEFT: int
		LEFT: int


	Type = ResourceType


	def __init__(self, id: int, coordinate: Tuple[int, int], type: int, value: int):
		self.id: int = id
		self.coordinate: list[int, int] = coordinate.copy()
		# Abstract parts
		self.roads: list[Road] = [None, None, None, None, None, None]
		self.settlements: list[Settlement] = [None, None, None, None, None, None]
		# Game parts
		self.type: int = type
		self.value: int = value


	def __eq__(self, right: Tile) -> bool:
		return self.id == right.id


	def __iter__(self) -> iter:
		yield from {
			"id": self.id,
			"Roads": {
				f"Tile::Roads::{self.Roads.ENUM_KEYS[index]}": road.id
				for index, road in enumerate(self.roads)
				if(road)
			},
			"Settlements": {
				f"Tile::Settlements::{self.Settlements.ENUM_KEYS[index]}": settlement.id
				for index, settlement in enumerate(self.settlements)
				if(settlement)
			}
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		def center(value: int, space_length: int=3, padder: str=' ') -> str:
			value_string: str = str(value)
			value_length: int = len(value_string)

			if(value_length >= space_length):
				return value_string

			else:
				length_difference: int = space_length - value_length
				side_padding_length: int = length_difference // 2
				additional_padding: int = length_difference - (side_padding_length * 2)

				side_padding: str = padder * side_padding_length
				return f"""{side_padding}{value_string}{padder * additional_padding}{side_padding}"""


		id: str = center(self.id)
		b_tl: str = center(self.roads[self.Roads.TOP_LEFT].id)
		b_t_: str = center(self.roads[self.Roads.TOP].id, padder='_')
		b_tr: str = center(self.roads[self.Roads.TOP_RIGHT].id)
		b_br: str = center(self.roads[self.Roads.BOTTOM_RIGHT].id)
		b_b_: str = center(self.roads[self.Roads.BOTTOM].id, padder='_')
		b_bl: str = center(self.roads[self.Roads.BOTTOM_LEFT].id)

		c_tl: str = f"""{self.settlements[self.Settlements.TOP_LEFT].id or "":>3}"""
		c_tr: str = self.settlements[self.Settlements.TOP_RIGHT].id or ""
		c_r_: str = self.settlements[self.Settlements.RIGHT].id or ""
		c_br: str = self.settlements[self.Settlements.BOTTOM_RIGHT].id or ""
		c_bl: str = f"""{self.settlements[self.Settlements.BOTTOM_LEFT].id or "":>3}"""
		c_l_: str = f"""{self.settlements[self.Settlements.LEFT].id or "":>3}"""
		return (
			r"   {a}___{b}___{c}   " "\n"
			r"     /         \     " "\n"
			r"   {d}         {e}   " "\n"
			r"{f}/     {g}     \{h}" "\n"
			r"   \             /   " "\n"
			r"   {i}         {j}   " "\n"
			r"     \___{k}___/     " "\n"
			r"   {l}         {m}"
		).format(a=c_tl, b=b_t_, c=c_tr, d=b_tl, e=b_tr, f=c_l_, g=id, h=c_r_, i=b_bl, j=b_br, k=b_b_, l=c_bl, m=c_br)
