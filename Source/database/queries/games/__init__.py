#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.05.12                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from database.queries.games.get import get_game
from database.queries.games.get import get_board
from database.queries.games.get import get_ports
from database.queries.games.get import get_roads
from database.queries.games.get import get_settlements
from database.queries.games.get import get_tiles
from database.queries.games.get import get_robber

from database.queries.games.new import new_game
from database.queries.games.new.board import new_board
from database.queries.games.new.board import new_port
from database.queries.games.new.board import new_ports
from database.queries.games.new.board import new_road
from database.queries.games.new.board import new_roads
from database.queries.games.new.board import new_robber
from database.queries.games.new.board import new_settlement
from database.queries.games.new.board import new_settlements
from database.queries.games.new.board import new_tile
from database.queries.games.new.board import new_tiles

from database.queries.games.update import update_port_settlements
