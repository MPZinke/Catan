

from board import Port, Road, Settlement, Tile


def create_ports(port_dicts: list[dict]) -> list[Port]:
	ports: list[Port] = []
	for port_dict in port_dicts:
		print(port_dict)
		ports.append(Port(port_dict["id"], port_dict["ResourceTypes.id"]-1))

	return ports


def create_roads(road_dicts: list[dict]) -> list[Road]:
	roads: list[Road] = []
	for road_dict in road_dicts:
		roads.append(Road(road_dict["id"]))

	return roads


def create_settlements(settlement_dicts: list[dict]) -> list[Settlement]:
	settlements: list[Settlement] = []
	for settlement_dict in settlement_dicts:
		settlements.append(Settlement(settlement_dict["id"]))

	return settlements


def create_tiles(tile_dicts: list[dict]) -> list[Tile]:
	tiles: list[Tile] = []
	for tile_dict in tile_dicts:
		tiles.append(Tile(tile_dict["id"], tile_dict["coordinate"], tile_dict["ResourceTypes.id"]-1, tile_dict["value"]))

	return tiles
