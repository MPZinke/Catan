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
from typing import Optional, Tuple, TypeVar


from database.queries import directions, types
from Enum import Enum


Road = TypeVar("Road")
Roads = list[Optional[Road]]
Settlement = TypeVar("Settlement")
Settlements = list[Optional[Settlement]]
Tile = TypeVar("Tile")
Tiles = list[Optional[Tile]]


class Tile:
	Roads = Enum("Tile::Roads", **{type["label"]: type["id"]-1 for type in directions.get_side_edges()})
	r"""
	Roads relative to hexagon
	 Roads
	  4  3  2
	   \ | / 
	     ⬣
	   / | \
	  5  0  1
	"""


	Settlements = Enum("Tile::Settlements", **{type["label"]: type["id"]-1 for type in directions.get_side_corners()})
	r"""
	Settlements relative to hexagon
	   4    3
	    \  / 
	 5 — ⬣ — 2
	    /  \
	   0    1
	"""


	ResourceTypes = Enum("Tile::ResourceTypes", **{type["label"]: type["id"]-1 for type in types.get_resource_types()})


	def __init__(self, id: int, coordinate: Tuple[int, int], type: int, value: int):
		self.id: int = id
		self.coordinate: list[int, int] = coordinate.copy()
		# Abstract parts
		self.roads: Roads = [None for _ in range(self.Roads.length)]
		self.settlements: Settlements = [None for _ in range(self.Settlements.length)]
		# Game parts
		self.type: int = type
		self.value: int = value


	def __eq__(self, right: Tile) -> bool:
		if(right is None):
			return False

		return self.id == right.id


	# def __iter__(self) -> iter:
	# 	yield from {
	# 		"id": self.id,
	# 		"TemplatesRoads": {
	# 			f"Tile::Roads::{self.Roads.ENUM_KEYS[index]}": road.id
	# 			for index, road in enumerate(self.roads)
	# 			if(road)
	# 		},
	# 		"TemplatesSettlements": {
	# 			f"Tile::Settlements::{self.Settlements.ENUM_KEYS[index]}": settlement.id
	# 			for index, settlement in enumerate(self.settlements)
	# 			if(settlement)
	# 		}
	# 	}.items()


	# def __repr__(self) -> str:
	# 	return str(self)


	# def __str__(self) -> str:
	# 	def center(value: int, space_length: int=3, padder: str=' ') -> str:
	# 		value_string: str = str(value)
	# 		value_length: int = len(value_string)

	# 		if(value_length >= space_length):
	# 			return value_string

	# 		else:
	# 			length_difference: int = space_length - value_length
	# 			side_padding_length: int = length_difference // 2
	# 			additional_padding: int = length_difference - (side_padding_length * 2)

	# 			side_padding: str = padder * side_padding_length
	# 			return f"""{side_padding}{value_string}{padder * additional_padding}{side_padding}"""


	# 	id: str = center(self.id)
	# 	r_tl: str = center(self.roads[self.Roads.TOP_LEFT].id)
	# 	r_t_: str = center(self.roads[self.Roads.TOP].id, padder='_')
	# 	r_tr: str = center(self.roads[self.Roads.TOP_RIGHT].id)
	# 	r_br: str = center(self.roads[self.Roads.BOTTOM_RIGHT].id)
	# 	r_b_: str = center(self.roads[self.Roads.BOTTOM].id, padder='_')
	# 	r_bl: str = center(self.roads[self.Roads.BOTTOM_LEFT].id)

	# 	s_tl: str = f"""{self.settlements[self.Settlements.TOP_LEFT].id or "-":>3}"""
	# 	s_tr: str = self.settlements[self.Settlements.TOP_RIGHT].id or "-"
	# 	s_r_: str = self.settlements[self.Settlements.RIGHT].id or "-"
	# 	s_br: str = self.settlements[self.Settlements.BOTTOM_RIGHT].id or "-"
	# 	s_bl: str = f"""{self.settlements[self.Settlements.BOTTOM_LEFT].id or "-":>3}"""
	# 	s_l_: str = f"""{self.settlements[self.Settlements.LEFT].id or "-":>3}"""
	# 	return (
	# 		r"   {a}___{b}___{c}   " "\n"
	# 		r"     /         \     " "\n"
	# 		r"   {d}         {e}   " "\n"
	# 		r"{f}/     {g}     \{h}" "\n"
	# 		r"   \             /   " "\n"
	# 		r"   {i}         {j}   " "\n"
	# 		r"     \___{k}___/     " "\n"
	# 		r"   {l}         {m}   " "\n"
	# 	).format(a=s_tl, b=r_t_, c=s_tr, d=r_tl, e=r_tr, f=s_l_, g=id, h=s_r_, i=r_bl, j=r_br, k=r_b_, l=s_bl, m=s_br)


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"coordinate": self.coordinate,
			"type": self.type,
			"value": self.value,
			"roads": [road.id if(road) else None for road in self.roads],
			"settlements": [settlement.id if(settlement) else None for settlement in self.settlements],
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4)
