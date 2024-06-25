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


from typing import Optional


DictList = list[dict]


class BoardData:
	def __init__(self, *,
		id: Optional[int]=None,
		board_id: Optional[int]=None,
		ports: Optional[DictList]=None,
		ports_settlements: Optional[DictList]=None,
		roads: Optional[DictList]=None,
		roads_settlements: Optional[DictList]=None,
		roads_tiles: Optional[DictList]=None,
		robber: Optional[dict]=None,
		settlements: Optional[DictList]=None,
		settlements_tiles: Optional[DictList]=None,
		tiles: Optional[DictList]=None,
	):
		self.id: Optional[int] = id
		self.board_id: Optional[int] = board_id
		self.ports: Optional[DictList] = ports
		self.ports_settlements: Optional[DictList] = ports_settlements
		self.roads: Optional[DictList] = roads
		self.roads_settlements: Optional[DictList] = roads_settlements
		self.roads_tiles: Optional[DictList] = roads_tiles
		self.robber: Optional[DictList] = robber
		self.settlements: Optional[DictList] = settlements
		self.settlements_tiles: Optional[DictList] = settlements_tiles
		self.tiles: Optional[DictList] = tiles
