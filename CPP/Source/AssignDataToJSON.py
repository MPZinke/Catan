

import json


relationships = [
	[0, 0, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[0, 1, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[0, 4, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[0, 9, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[0, 8, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[0, 3, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],
	
	[1, 2, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[1, 3, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[1, 8, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[1, 14, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[1, 13, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[1, 7, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[2, 4, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[2, 5, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[2, 10, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[2, 16, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[2, 15, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[2, 9, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[3, 6, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[3, 7, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[3, 13, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[3, 19, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[3, 18, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[3, 12, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[4, 8, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[4, 9, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[4, 15, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[4, 21, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[4, 20, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[4, 14, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[5, 10, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[5, 11, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[5, 17, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[5, 23, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[5, 22, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[5, 16, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[6, 13, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[6, 14, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[6, 20, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[6, 26, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[6, 25, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[6, 19, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[7, 15, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[7, 16, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[7, 22, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[7, 28, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[7, 27, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[7, 21, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[8, 18, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[8, 19, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[8, 25, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[8, 31, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[8, 30, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[8, 24, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[9, 20, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[9, 21, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[9, 27, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[9, 33, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[9, 32, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[9, 26, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[10, 22, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[10, 23, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[10, 29, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[10, 35, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[10, 34, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[10, 28, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[11, 25, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[11, 26, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[11, 32, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[11, 38, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[11, 37, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[11, 31, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[12, 27, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[12, 28, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[12, 34, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[12, 40, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[12, 39, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[12, 33, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[13, 30, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[13, 31, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[13, 37, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[13, 43, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[13, 42, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[13, 36, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[14, 32, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[14, 33, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[14, 39, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[14, 45, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[14, 44, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[14, 38, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[15, 34, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[15, 35, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[15, 41, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[15, 47, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[15, 46, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[15, 40, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[16, 37, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[16, 38, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[16, 44, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[16, 49, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[16, 48, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[16, 43, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[17, 39, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[17, 40, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[17, 46, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[17, 51, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[17, 50, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[17, 45, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"],

	[18, 44, "Hexagon::Corners::BOTTOM_LEFT", "Corner::Hexagons::TOP"],
	[18, 45, "Hexagon::Corners::BOTTOM_RIGHT", "Corner::Hexagons::TOP"],
	[18, 50, "Hexagon::Corners::RIGHT", "Corner::Hexagons::SIDE"],
	[18, 53, "Hexagon::Corners::TOP_RIGHT", "Corner::Hexagons::BOTTOM"],
	[18, 52, "Hexagon::Corners::TOP_LEFT", "Corner::Hexagons::BOTTOM"],
	[18, 49, "Hexagon::Corners::LEFT", "Corner::Hexagons::SIDE"]
]


HexagonID = 0
CornerID = 1
HexagonsCornerIndex = 2
CornersHexagonIndex = 3


with open("GameData.json", "r") as file:
	data = json.load(file)

for relation in relationships:
	hexagon_id = relation[HexagonID]
	corner_id = relation[CornerID]
	hexagon = next(hexagon for hexagon in data["Hexagons"] if(hexagon["id"] == hexagon_id))
	corner = next(corner for corner in data["Corners"] if(corner["id"] == corner_id))
	if("Corners" not in hexagon):
		hexagon["Corners"] = {}
	if("Hexagons" not in corner):
		corner["Hexagons"] = {}

	hexagon["Corners"][relation[HexagonsCornerIndex]] = corner_id
	corner["Hexagons"][relation[CornersHexagonIndex]] = hexagon_id

with open("GameData2.json", "w") as file:
	file.write(json.dumps(data, indent=4))
