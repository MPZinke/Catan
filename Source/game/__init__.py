#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.27                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from database import queries
from game.player.Player import Player, Players
from game.Game import Game


def game(game_id: int) -> Game:
	game_dict: dict = queries.games.get_game(game_id)
	port_dicts: list[dict] = queries.games.get_ports(game_id)
	roads_dicts: list[dict] = queries.games.get_roads(game_id)
	settlements_dicts: list[dict] = queries.games.get_settlements(game_id)
	tiles_dicts: list[dict] = queries.games.get_tiles(game_id)

	
