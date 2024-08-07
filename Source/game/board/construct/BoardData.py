#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.06.24                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from typing import Optional, Tuple


DictList = list[dict]


class BoardData:
	def __init__(self, *,
		id: Optional[int]=None,
		size: Optional[Tuple[int, int]]=None,
		game_id: Optional[int]=None,
		template_id: Optional[int]=None,
		ports: Optional[DictList]=None,
		roads: Optional[DictList]=None,
		robber: Optional[dict]=None,
		settlements: Optional[DictList]=None,
		tiles: Optional[DictList]=None,
	):
		self.id: Optional[int] = id
		self.size: Optional[Tuple[int, int]] = size
		self.game_id: Optional[int] = game_id
		self.template_id: Optional[int] = template_id
		self.ports: Optional[DictList] = ports
		self.roads: Optional[DictList] = roads
		self.robber: Optional[DictList] = robber
		self.settlements: Optional[DictList] = settlements
		self.tiles: Optional[DictList] = tiles
