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
		ports: Optional[DictList]=None,
		roads: Optional[DictList]=None,
		robber: Optional[dict]=None,
		settlements: Optional[DictList]=None,
		tiles: Optional[DictList]=None,
	):
		self.ports: Optional[DictList] = ports
		self.roads: Optional[DictList] = roads
		self.robber: Optional[DictList] = robber
		self.settlements: Optional[DictList] = settlements
		self.tiles: Optional[DictList] = tiles
