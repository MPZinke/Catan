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


Border = TypeVar("Border")
Corner = TypeVar("Corner")
Tile = TypeVar("Tile")


class Tile:
	class Borders(Enum):
		r"""
		Borders relative to hexagon
		 Borders
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


	class Corners(Enum):
		r"""
		Corners relative to hexagon
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


	class Type(Enum):
		DESERT: int
		WHEAT: int
		WOOD: int
		SHEEP: int
		STONE: int
		BRICK: int


	def __init__(self, id: int, coordinate: Tuple[int, int], type: int, value: int):
		self.id: int = id
		self.coordinate: list[int, int] = coordinate.copy()
		self.type: int = type
		self.value: int = value
		self.borders: list[Border] = [None, None, None, None, None, None]
		self.corners: list[Corner] = [None, None, None, None, None, None]


	def __iter__(self) -> iter:
		yield from {
			"id": self.id,
			"Borders": {
				f"Tile::Borders::{self.Borders.ENUM_KEYS[index]}": border.id
				for index, border in enumerate(self.borders)
				if(border)
			},
			"Corners": {
				f"Tile::Corners::{self.Corners.ENUM_KEYS[index]}": corner.id
				for index, corner in enumerate(self.corners)
				if(corner)
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
		b_tl: str = center(self.borders[self.Borders.TOP_LEFT].id)
		b_t_: str = center(self.borders[self.Borders.TOP].id, padder='_')
		b_tr: str = center(self.borders[self.Borders.TOP_RIGHT].id)
		b_br: str = center(self.borders[self.Borders.BOTTOM_RIGHT].id)
		b_b_: str = center(self.borders[self.Borders.BOTTOM].id, padder='_')
		b_bl: str = center(self.borders[self.Borders.BOTTOM_LEFT].id)

		c_tl: str = f"""{self.corners[self.Corners.TOP_LEFT].id or "":>3}"""
		c_tr: str = self.corners[self.Corners.TOP_RIGHT].id or ""
		c_r_: str = self.corners[self.Corners.RIGHT].id or ""
		c_br: str = self.corners[self.Corners.BOTTOM_RIGHT].id or ""
		c_bl: str = f"""{self.corners[self.Corners.BOTTOM_LEFT].id or "":>3}"""
		c_l_: str = f"""{self.corners[self.Corners.LEFT].id or "":>3}"""
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
