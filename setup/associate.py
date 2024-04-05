

from board import Port
from board import Road
from board import Settlement
from board import Tile


def find(id: int) -> callable:
	def callback(item: object) -> bool:
		return item.id == id

	return callback


def ports_with_settlements(port_dicts: list[dict], ports: list[Port], settlements: list[Settlement]):
	for port_dict in port_dicts:
		port = next(filter(find(port_dict["id"]), ports))
		for settlement_direction, settlement_id in port_dict["Settlements"].items():
			settlement = next(filter(find(settlement_id), settlements))
			direction_index = Port.Settlements.ENUM_VALUES[settlement_direction.split("::")[2]]
			port.settlements[direction_index] = settlement


def roads_with_settlements(road_dicts: list[dict], roads: list[Road], settlements: list[Settlement]):
	for road_dict in road_dicts:
		road = next(filter(find(road_dict["id"]), roads))
		for settlement_direction, settlement_id in road_dict["Settlements"].items():
			settlement = next(filter(find(settlement_id), settlements))
			direction_index = Road.Settlements.ENUM_VALUES[settlement_direction.split("::")[2]]
			road.settlements[direction_index] = settlement


def roads_with_tiles(road_dicts: list[dict], roads: list[Road], tiles: list[Tile]):
	for road_dict in road_dicts:
		road = next(filter(find(road_dict["id"]), roads))
		for tile_direction, tile_id in road_dict["Tiles"].items():
			tile = next(filter(find(tile_id), tiles))
			direction_index = Road.Tiles.ENUM_VALUES[tile_direction.split("::")[2]]
			road.tiles[direction_index] = tile


def settlements_with_ports(settlement_dicts: list[dict], settlements: list[Settlement], ports: list[Road]):
	for settlement_dict in settlement_dicts:
		settlement = next(filter(find(settlement_dict["id"]), settlements))
		for port_direction, port_id in settlement_dict["Ports"].items():
			print(settlement.id, port_id)
			port = next(filter(find(port_id), ports))
			direction_index = Settlement.Ports.ENUM_VALUES[port_direction.split("::")[2]]
			settlement.ports[direction_index] = port


def settlements_with_roads(settlement_dicts: list[dict], settlements: list[Settlement], roads: list[Road]):
	for settlement_dict in settlement_dicts:
		settlement = next(filter(find(settlement_dict["id"]), settlements))
		for road_direction, road_id in settlement_dict["Roads"].items():
			road = next(filter(find(road_id), roads))
			direction_index = Settlement.Roads.ENUM_VALUES[road_direction.split("::")[2]]
			settlement.roads[direction_index] = road


def settlements_with_tiles(settlement_dicts: list[dict], settlements: list[Settlement], tiles: list[Settlement]):
	for settlement_dict in settlement_dicts:
		settlement = next(filter(find(settlement_dict["id"]), settlements))
		for tile_direction, tile_id in settlement_dict["Tiles"].items():
			tile = next(filter(find(tile_id), tiles))
			direction_index = Settlement.Tiles.ENUM_VALUES[tile_direction.split("::")[2]]
			settlement.tiles[direction_index] = tile


def tiles_with_roads(tile_dicts: list[dict], tiles: list[Tile], roads: list[Road]):
	for tile_dict in tile_dicts:
		tile = next(filter(find(tile_dict["id"]), tiles))
		for road_direction, road_id in tile_dict["Roads"].items():
			road = next(filter(find(road_id), roads))
			direction_index = Tile.Roads.ENUM_VALUES[road_direction.split("::")[2]]
			tile.roads[direction_index] = road


def tiles_with_settlements(tile_dicts: list[dict], tiles: list[Road], settlements: list[Settlement]):
	for tile_dict in tile_dicts:
		tile = next(filter(find(tile_dict["id"]), tiles))
		for settlement_direction, settlement_id in tile_dict["Settlements"].items():
			settlement = next(filter(find(settlement_id), settlements))
			direction_index = Tile.Settlements.ENUM_VALUES[settlement_direction.split("::")[2]]
			tile.settlements[direction_index] = settlement
