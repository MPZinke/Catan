#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.07.27                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
#########################################################################################################################!/opt/homebrew/bin/python3


import os
from pathlib import Path


from flask import Blueprint


from constants import directions, player_colors, resource_types
import game


ROOT_DIR = str(Path(__file__).absolute().parent.parent)
TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "Webpage")
STATIC_FOLDER = os.path.join(ROOT_DIR, "Webpage/Static")


api_blueprint = Blueprint('api_blueprint', __name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)


@api_blueprint.route("/api/constants")
def api_constants() -> dict:
	return {
		"directions": directions(),
		"player_colors": player_colors(),
		"resource_types": resource_types()
	}
