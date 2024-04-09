

from board import Port
from board import Road
from board import Settlement
from board import Tile


def find(id: int) -> callable:
	def callback(item: object) -> bool:
		return item.id == id

	return callback


def ports_and_settlements(ports_settlements_dicts: list[dict], ports: list[Port], settlements: list[Settlement]):
	for ports_settlements_dict in ports_settlements_dicts:
		port = next(filter(find(ports_settlements_dict["Ports.id"]), ports))
		settlement = next(filter(find(ports_settlements_dict["Settlements.id"]), settlements))
		port.settlements[ports_settlements_dict["Side's Corners.id"]-1] = settlement
		settlement.ports[ports_settlements_dict["Corner's Sides.id"]-1] = port


def roads_and_settlements(roads_settlements_dicts: list[dict], roads: list[Port], settlements: list[Settlement]):
	for roads_settlements_dict in roads_settlements_dicts:
		road = next(filter(find(roads_settlements_dict["Roads.id"]), roads))
		settlement = next(filter(find(roads_settlements_dict["Settlements.id"]), settlements))
		road.settlements[roads_settlements_dict["Edge's Corners.id"]-1] = settlement
		settlement.roads[roads_settlements_dict["Corner's Edges.id"]-1] = road


def roads_and_tiles(roads_tiles_dicts: list[dict], roads: list[Port], tiles: list[Settlement]):
	for roads_tiles_dict in roads_tiles_dicts:
		road = next(filter(find(roads_tiles_dict["Roads.id"]), roads))
		tile = next(filter(find(roads_tiles_dict["Tiles.id"]), tiles))
		road.tiles[roads_tiles_dict["Edge's Sides.id"]-1] = tile
		tile.roads[roads_tiles_dict["Side's Edges.id"]-1] = road


def settlements_and_tiles(settlements_tiles_dicts: list[dict], settlements: list[Port], tiles: list[Settlement]):
	for settlements_tiles_dict in settlements_tiles_dicts:
		settlement = next(filter(find(settlements_tiles_dict["Settlements.id"]), settlements))
		tile = next(filter(find(settlements_tiles_dict["Tiles.id"]), tiles))
		settlement.tiles[settlements_tiles_dict["Corner's Sides.id"]-1] = tile
		tile.settlements[settlements_tiles_dict["Side's Corners.id"]-1] = settlement
