"""Coverts template parts from Associated N:M mappings to Array based associations"""


from game.board.template import template_data

from database.queries.directions import (
	get_corner_edges,  # Settlement-Roads
	get_corner_sides,  # Settlement-Ports  # Settlement-Tiles
	get_edge_corners,  # Road-Settlements
	get_edge_sides,  # Road-Tiles
	get_side_corners,  # Port-Settlements  # Tile-Settlements
	get_side_edges,  # Tile-Roads
)


def port_settlement_ids(template, port_id: int) -> list[int]:
	side_corners_dicts = get_side_corners()
	settlement_ids = [None for _ in side_corners_dicts]

	for ports_settlement in template.ports_settlements:
		if(ports_settlement["TemplatesPorts.id"] == port_id):
			settlement_ids[ports_settlement["Side's Corners.id"]-1] = ports_settlement["TemplatesSettlements.id"]

	return settlement_ids


def print_ports(template):
	query = """INSERT INTO "TemplatesPorts" ("Templates.id", "ResourceTypes.id", "TemplatesSettlements.ids") VALUES\n"""
	values = []
	for port_dict in template.ports:
		settlement_ids = port_settlement_ids(template, port_dict["id"])
		value = f"""({template.id}, {port_dict["ResourceTypes.id"]}, ARRAY{settlement_ids}::INT[6])"""
		values.append(value)

	query += ",\n".join(values) + ";\n\n"
	print(query)





def roads_settlements_ids(template, road_id: int) -> list[int]:
	edge_corners_dicts = get_edge_corners()
	settlement_ids = [None for _ in edge_corners_dicts]

	for roads_settlements in template.roads_settlements:
		if(roads_settlements["TemplatesRoads.id"] == road_id):
			settlement_ids[roads_settlements["Edge's Corners.id"]-1] = roads_settlements["TemplatesSettlements.id"]

	return settlement_ids


def roads_tiles_ids(template, road_id: int) -> list[int]:
	corner_sides_dicts = get_edge_sides()
	tile_ids = [None for _ in corner_sides_dicts]

	for roads_tile in template.roads_tiles:
		if(roads_tile["TemplatesRoads.id"] == road_id):
			tile_ids[roads_tile["Edge's Sides.id"]-1] = roads_tile["TemplatesTiles.id"]

	return tile_ids


def print_roads(template):
	query = """INSERT INTO "TemplatesRoads" ("Templates.id", "TemplatesSettlements.ids", "TemplatesTiles.ids") VALUES\n"""
	values = []
	for road_dict in template.roads:
		roads_ids = roads_settlements_ids(template, road_dict["id"])
		tiles_ids = roads_tiles_ids(template, road_dict["id"])
		value = f"""({template.id}, ARRAY{roads_ids}::INT[2], ARRAY{tiles_ids}::INT[2])"""
		values.append(value)

	query += ",\n".join(values) + ";\n\n"
	print(query)




def settlements_ports_ids(template, settlement_id: int) -> list[int]:
	corner_sides_dicts = get_corner_sides()
	port_ids = [None for _ in corner_sides_dicts]

	for settlements_port in template.ports_settlements:
		if(settlements_port["TemplatesSettlements.id"] == settlement_id):
			port_ids[settlements_port["Corner's Sides.id"]-1] = settlements_port["TemplatesPorts.id"]

	return port_ids


def settlements_roads_ids(template, settlement_id: int) -> list[int]:
	corner_edges_dicts = get_corner_edges()
	road_ids = [None for _ in corner_edges_dicts]

	for settlements_roads in template.roads_settlements:
		if(settlements_roads["TemplatesSettlements.id"] == settlement_id):
			road_ids[settlements_roads["Corner's Edges.id"]-1] = settlements_roads["TemplatesRoads.id"]

	return road_ids


def settlements_tiles_ids(template, settlement_id: int) -> list[int]:
	corner_sides_dicts = get_corner_sides()
	tile_ids = [None for _ in corner_sides_dicts]

	for settlements_tile in template.settlements_tiles:
		if(settlements_tile["TemplatesSettlements.id"] == settlement_id):
			tile_ids[settlements_tile["Corner's Sides.id"]-1] = settlements_tile["TemplatesTiles.id"]

	return tile_ids


def print_settlements(template):
	query = """INSERT INTO "TemplatesSettlements" ("Templates.id", "TemplatesPorts.ids", "TemplatesRoads.ids", "TemplatesTiles.ids") VALUES\n"""
	values = []
	for settlement_dict in template.settlements:
		ports_ids = settlements_ports_ids(template, settlement_dict["id"])
		roads_ids = settlements_roads_ids(template, settlement_dict["id"])
		tiles_ids = settlements_tiles_ids(template, settlement_dict["id"])
		value = f"""({template.id}, ARRAY{ports_ids}::INT[3], ARRAY{roads_ids}::INT[3], ARRAY{tiles_ids}::INT[3])"""
		values.append(value)

	query += ",\n".join(values) + ";\n\n"
	print(query)




def tiles_roads_ids(template, tile_id: int) -> list[int]:
	side_edges_dicts = get_side_edges()
	road_ids = [None for _ in side_edges_dicts]

	for tiles_roads in template.roads_tiles:
		if(tiles_roads["TemplatesTiles.id"] == tile_id):
			road_ids[tiles_roads["Side's Edges.id"]-1] = tiles_roads["TemplatesRoads.id"]

	return road_ids


def tiles_settlements_ids(template, tile_id: int) -> list[int]:
	side_corners_dicts = get_side_corners()
	settlement_ids = [None for _ in side_corners_dicts]

	for tiles_settlements in template.settlements_tiles:
		if(tiles_settlements["TemplatesTiles.id"] == tile_id):
			settlement_ids[tiles_settlements["Side's Corners.id"]-1] = tiles_settlements["TemplatesSettlements.id"]

	return settlement_ids


def print_tiles(template):
	query = """INSERT INTO "TemplatesTiles" ("Templates.id", "coordinate", "count", "ResourceTypes.id", "TemplatesRoads.ids", "TemplatesSettlements.ids") VALUES\n"""
	values = []
	for tile_dict in template.tiles:
		roads_ids = tiles_roads_ids(template, tile_dict["id"])
		settlements_ids = tiles_settlements_ids(template, tile_dict["id"])
		value = f"""({template.id}, ARRAY{tile_dict["coordinate"]}::INT[2], {tile_dict["count"]}, {tile_dict["ResourceTypes.id"]}, ARRAY{roads_ids}::INT[6], ARRAY{settlements_ids}::INT[6])"""
		values.append(value)

	query += ",\n".join(values) + ";\n\n"
	print(query)




template = template_data(1)
print_ports(template)
print_roads(template)
print_settlements(template)
print_tiles(template)
