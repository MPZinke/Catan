

import json


def road_settlements(data: dict):
	road_settlement_associations = []
	for road in data["Board"]["Roads"]:
		for settlement_direction, settlement_id in road["Settlements"].items():
			association = {
				"board": "Board 1",
				"Road": road["id"] + 1,
				"Edge's Corner": settlement_direction.split("::")[2],
				"Settlement": settlement_id + 1
			}

			road_settlement_associations.append(association)

			for settlement in data["Board"]["Settlements"]:
				if(settlement["id"] != settlement_id):
					continue

				for road_direction, road_id in settlement["Roads"].items():
					if(road_id == road["id"]):
						association["Corner's Edge"] = road_direction.split("::")[2]

	print(
		"""INSERT INTO "RoadsSettlements" (\n"""
		"""	"Boards.id", "Corner's Edges.id", "Edge's Corners.id", "Roads.id", "Settlements.id"\n"""
		""")\n"""
		"""SELECT "Boards"."id", "Corner's Edges"."id", "Edge's Corners"."id", T."Roads.id", T."Settlements.id"\n"""
		"""FROM \n"""
		"""(\n"""
		"""	VALUES"""
	)

	for x, road in enumerate(road_settlement_associations):
		end = ",\n" if(x < len(road_settlement_associations) - 1) else "\n"
		print(f"""\t('Board 1', '{road["Corner's Edge"]}', '{road["Edge's Corner"]}', {road["Road"]}, {road["Settlement"]})""", end=end)

	print(
		""") AS T ("Boards.name", "Corner's Edges.label", "Edge's Corners.label", "Roads.id", "Settlements.id")\n"""
		"""JOIN "Boards" ON T."Boards.name" = "Boards"."name"\n"""
		"""JOIN "Corner's Edges" ON T."Corner's Edges.label" = "Corner's Edges"."label"\n"""
		"""JOIN "Edge's Corners" ON T."Edge's Corners.label" = "Edge's Corners"."label";\n"""
	)


def road_tiles(data: dict):
	road_tile_associations = []
	for road in data["Board"]["Roads"]:
		for tile_direction, tile_id in road["Tiles"].items():
			association = {
				"board": "Board 1",
				"Road": road["id"] + 1,
				"Edge's Side": tile_direction.split("::")[2],
				"Tile": tile_id + 1
			}

			road_tile_associations.append(association)

			for tile in data["Board"]["Tiles"]:
				if(tile["id"] != tile_id):
					continue

				for road_direction, road_id in tile["Roads"].items():
					if(road_id == road["id"]):
						association["Side's Edge"] = road_direction.split("::")[2]

	print(
		"""INSERT INTO "RoadsTiles" (\n"""
		"""	"Boards.id", "Side's Edges.id", "Edge's Sides.id", "Roads.id", "Tiles.id"\n"""
		""")\n"""
		"""SELECT "Boards"."id", "Side's Edges"."id", "Edge's Sides"."id", T."Roads.id", T."Tiles.id"\n"""
		"""FROM \n"""
		"""(\n"""
		"""	VALUES"""
	)
	for x, road in enumerate(road_tile_associations):
		end = ",\n" if(x < len(road_tile_associations) - 1) else "\n"
		print(f"""\t('Board 1', '{road["Side's Edge"]}', '{road["Edge's Side"]}', {road["Road"]}, {road["Tile"]})""", end=end)

	print(
		""") AS T ("Boards.name", "Side's Edges.label", "Edge's Sides.label", "Roads.id", "Tiles.id")\n"""
		"""JOIN "Boards" ON T."Boards.name" = "Boards"."name"\n"""
		"""JOIN "Side's Edges" ON T."Side's Edges.label" = "Side's Edges"."label"\n"""
		"""JOIN "Edge's Sides" ON T."Edge's Sides.label" = "Edge's Sides"."label";\n"""
	)


def settlement_ports(data: dict):
	settlement_port_associations = []
	for settlement in data["Board"]["Settlements"]:
		for port_direction, port_id in settlement["Ports"].items():
			association = {
				"board": "Board 1",
				"Settlement": settlement["id"] + 1,
				"Corner's Side": port_direction.split("::")[2],
				"Port": port_id + 1
			}

			settlement_port_associations.append(association)

			for port in data["Board"]["Ports"]:
				if(port["id"] != port_id):
					continue

				for settlement_direction, settlement_id in port["Settlements"].items():
					if(settlement_id == settlement["id"]):
						association["Side's Corner"] = settlement_direction.split("::")[2]

	print(
		"""INSERT INTO "PortsSettlements" (\n"""
		"""	"Boards.id", "Side's Corners.id", "Corner's Sides.id", "Settlements.id", "Ports.id"\n"""
		""")\n"""
		"""SELECT "Boards"."id", "Side's Corners"."id", "Corner's Sides"."id", T."Settlements.id", T."Ports.id"\n"""
		"""FROM \n"""
		"""(\n"""
		"""	VALUES"""
	)

	for x, settlement in enumerate(settlement_port_associations):
		end = ",\n" if(x < len(settlement_port_associations) - 1) else "\n"
		print(f"""\t('Board 1', '{settlement["Side's Corner"]}', '{settlement["Corner's Side"]}', {settlement["Settlement"]}, {settlement["Port"]})""", end=end)

	print(
		""") AS T ("Boards.name", "Side's Corners.label", "Corner's Sides.label", "Settlements.id", "Ports.id")\n"""
		"""JOIN "Boards" ON T."Boards.name" = "Boards"."name"\n"""
		"""JOIN "Side's Corners" ON T."Side's Corners.label" = "Side's Corners"."label"\n"""
		"""JOIN "Corner's Sides" ON T."Corner's Sides.label" = "Corner's Sides"."label";\n"""
	)


def settlement_tiles(data: dict):
	settlement_tile_associations = []
	for settlement in data["Board"]["Settlements"]:
		for tile_direction, tile_id in settlement["Tiles"].items():
			association = {
				"board": "Board 1",
				"Settlement": settlement["id"] + 1,
				"Corner's Side": tile_direction.split("::")[2],
				"Tile": tile_id + 1
			}

			settlement_tile_associations.append(association)

			for tile in data["Board"]["Tiles"]:
				if(tile["id"] != tile_id):
					continue

				for settlement_direction, settlement_id in tile["Settlements"].items():
					if(settlement_id == settlement["id"]):
						association["Side's Corner"] = settlement_direction.split("::")[2]

	print(
		"""INSERT INTO "SettlementsTiles" (\n"""
		"""	"Boards.id", "Side's Corners.id", "Corner's Sides.id", "Settlements.id", "Tiles.id"\n"""
		""")\n"""
		"""SELECT "Boards"."id", "Side's Corners"."id", "Corner's Sides"."id", T."Settlements.id", T."Tiles.id"\n"""
		"""FROM \n"""
		"""(\n"""
		"""	VALUES"""
	)
	for x, settlement in enumerate(settlement_tile_associations):
		end = ",\n" if(x < len(settlement_tile_associations) - 1) else "\n"
		print(f"""\t('Board 1', '{settlement["Side's Corner"]}', '{settlement["Corner's Side"]}', {settlement["Settlement"]}, {settlement["Tile"]})""", end=end)

	print(
		""") AS T ("Boards.name", "Side's Corners.label", "Corner's Sides.label", "Settlements.id", "Tiles.id")\n"""
		"""JOIN "Boards" ON T."Boards.name" = "Boards"."name"\n"""
		"""JOIN "Side's Corners" ON T."Side's Corners.label" = "Side's Corners"."label"\n"""
		"""JOIN "Corner's Sides" ON T."Corner's Sides.label" = "Corner's Sides"."label";\n"""
	)


def main():
	with open("Data/BasicLayout.json") as file:
		data = json.load(file)

	# road_settlements(data)
	# road_tiles(data)
	# settlement_ports(data)
	settlement_tiles(data)


if(__name__ == "__main__"):
	main()
