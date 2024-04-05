

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

	for road in road_settlement_associations:
		print(f"""('Board 1', '{road["Corner's Edge"]}', '{road["Edge's Corner"]}', {road["Road"]}, {road["Settlement"]})""")


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

	for road in road_tile_associations:
		print(f"""('Board 1', '{road["Side's Edge"]}', '{road["Edge's Side"]}', {road["Road"]}, {road["Tile"]})""")


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

	for settlement in settlement_port_associations:
		print(f"""('Board 1', '{settlement["Side's Corner"]}', '{settlement["Corner's Side"]}', {settlement["Settlement"]}, {settlement["Port"]})""")


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

	for settlement in settlement_tile_associations:
		print(f"""('Board 1', '{settlement["Side's Corner"]}', '{settlement["Corner's Side"]}', {settlement["Settlement"]}, {settlement["Tile"]})""")


def main():
	with open("BasicLayout.json") as file:
		data = json.load(file)

	road_settlements(data)
	road_tiles(data)
	settlement_ports(data)
	settlement_tiles(data)


if(__name__ == "__main__"):
	main()
