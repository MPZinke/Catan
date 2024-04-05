

from board import Port
from board import Road
from board import Settlement
from board import Tile


def ports(port_dicts: list[dict]) -> list[Port]:
	ports_list: list[Port] = []
	for port_dict in port_dicts:
		type = Port.Types.ENUM_VALUES[port_dict["type"]]
		ports_list.append(Port(port_dict["id"], type))

	return ports_list


def roads(road_dicts: list[dict]) -> list[Road]:
	roads_list: list[Road] = []
	for road_dict in road_dicts:
		roads_list.append(Road(road_dict["id"]))

	return roads_list


def settlements(settlement_dicts: list[dict]) -> list[Settlement]:
	settlements_list: list[Settlement] = []
	for settlement_dict in settlement_dicts:
		settlements_list.append(Settlement(settlement_dict["id"]))

	return settlements_list


def tiles(tile_dicts: list[dict]) -> list[Tile]:
	tiles_list: list[Tile] = []
	for tile_dict in tile_dicts:
		type = Tile.Types.ENUM_VALUES[tile_dict["type"]]
		tiles_list.append(Tile(tile_dict["id"], tile_dict["coordinate"], type, tile_dict["value"]))

	return tiles_list
