

from board import Border
from board import Corner
from board import Tile


def borders(border_dicts: list[dict]) -> list[Border]:
	borders_list: list[Border] = []
	for border_dict in border_dicts:
		borders_list.append(Border(border_dict["id"]))

	return borders_list


def corners(corner_dicts: list[dict]) -> list[Corner]:
	corners_list: list[Corner] = []
	for corner_dict in corner_dicts:
		corners_list.append(Corner(corner_dict["id"]))

	return corners_list


def tiles(tile_dicts: list[dict]) -> list[Tile]:
	tiles_list: list[Tile] = []
	for tile_dict in tile_dicts:
		tiles_list.append(Tile(tile_dict["id"]))

	return tiles_list
