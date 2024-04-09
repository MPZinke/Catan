

import json


with open("BasicLayout.json", "r") as file:
	data = json.load(file)


fixed_data = {}

fixed_data["Board"] = {"Ports": data["Board"]["Ports"], "Roads": [], "Settlements": [], "Tiles": []}

for road in data["Board"]["Roads"]:
	fixed_road_data = {"id": road["id"], "Settlements": road["Settlements"], "Tiles": {}}
	for tile_direction, tile_id in road["Tiles"].items():
		fixed_direction = {
			"Road::Tiles::TOP": "Road::Tiles::BOTTOM",
			"Road::Tiles::BOTTOM": "Road::Tiles::TOP",
			"Road::Tiles::SIDE": "Road::Tiles::SIDE"
		}
		fixed_road_data["Tiles"][fixed_direction[tile_direction]] = tile_id

	fixed_data["Board"]["Roads"].append(fixed_road_data)

for settlement in data["Board"]["Settlements"]:
	fixed_settlement_data = {"id": settlement["id"], "Ports": settlement["Ports"], "Roads": {}, "Tiles": {}}
	for road_direction, road_id in settlement["Roads"].items():
		fixed_direction = {
			"Settlement::Roads::TOP": "Settlement::Roads::BOTTOM",
			"Settlement::Roads::BOTTOM": "Settlement::Roads::TOP",
			"Settlement::Roads::SIDE": "Settlement::Roads::SIDE"
		}
		fixed_settlement_data["Roads"][fixed_direction[road_direction]] = road_id

	fixed_settlement_data["Tiles"] = settlement["Tiles"]
	# for tile_direction, tile_id in settlement["Tiles"].items():
	# 	fixed_direction = {
	# 		"Settlement::Tiles::TOP": "Settlement::Tiles::BOTTOM",
	# 		"Settlement::Tiles::BOTTOM": "Settlement::Tiles::TOP",
	# 		"Settlement::Tiles::SIDE": "Settlement::Tiles::SIDE"
	# 	}
	# 	fixed_settlement_data["Tiles"][fixed_direction[tile_direction]] = tile_id

	fixed_data["Board"]["Settlements"].append(fixed_settlement_data)

for tile in data["Board"]["Tiles"]:
	fixed_settlement_data = {"id": tile["id"], "coordinate": tile["coordinate"], "Roads": {}, "Settlements": {}}
	for road_direction, road_id in tile["Roads"].items():
		fixed_direction = {
			"Tile::Roads::BOTTOM_LEFT": "Tile::Roads::TOP_LEFT",
			"Tile::Roads::BOTTOM_RIGHT": "Tile::Roads::TOP_RIGHT",
			"Tile::Roads::BOTTOM": "Tile::Roads::TOP",
			"Tile::Roads::TOP_RIGHT": "Tile::Roads::BOTTOM_RIGHT",
			"Tile::Roads::TOP_LEFT": "Tile::Roads::BOTTOM_LEFT",
			"Tile::Roads::TOP": "Tile::Roads::BOTTOM"
		}
		fixed_settlement_data["Roads"][fixed_direction[road_direction]] = road_id

	fixed_settlement_data["Settlements"] = tile["Settlements"]
	# for settlement_direction, settlement_id in tile["Settlements"].items():
	# 	fixed_direction = {
	# 		"Tile::Settlements::BOTTOM_LEFT": "Tile::Settlements::TOP_LEFT",
	# 		"Tile::Settlements::BOTTOM_RIGHT": "Tile::Settlements::TOP_RIGHT",
	# 		"Tile::Settlements::RIGHT": "Tile::Settlements::RIGHT",
	# 		"Tile::Settlements::TOP_RIGHT": "Tile::Settlements::BOTTOM_RIGHT",
	# 		"Tile::Settlements::TOP_LEFT": "Tile::Settlements::BOTTOM_LEFT",
	# 		"Tile::Settlements::LEFT": "Tile::Settlements::LEFT"
	# 	}
	# 	fixed_settlement_data["Settlements"][fixed_direction[settlement_direction]] = settlement_id

	fixed_data["Board"]["Tiles"].append(fixed_settlement_data)

with open("ConvertedData.json", "w") as file:
	file.write(json.dumps(fixed_data, indent=4))
