

import json


relationships = [
	[0, 0, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[0, 2, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[0, 7, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[0, 10, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[0, 6, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[0, 1, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[1, 3, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[1, 6, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[1, 14, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[1, 18, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[1, 13, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[1, 5, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[2, 4, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[2, 8, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[2, 16, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[2, 19, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[2, 15, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[2, 7, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[3, 9, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[3, 13, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[3, 21, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[3, 26, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[3, 20, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[3, 12, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[4, 10, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[4, 15, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[4, 23, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[4, 27, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[4, 22, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[4, 14, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[5, 11, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[5, 17, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[5, 25, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[5, 28, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[5, 24, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[5, 16, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[6, 18, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[6, 22, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[6, 31, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[6, 35, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[6, 30, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[6, 21, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[7, 19, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[7, 24, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[7, 33, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[7, 36, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[7, 32, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[7, 23, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[8, 26, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[8, 30, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[8, 38, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[8, 43, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[8, 37, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[8, 29, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[9, 27, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[9, 32, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[9, 40, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[9, 44, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[9, 39, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[9, 31, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[10, 28, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[10, 34, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[10, 42, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[10, 45, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[10, 41, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[10, 33, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[11, 35, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[11, 39, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[11, 48, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[11, 52, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[11, 47, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[11, 38, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[12, 36, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[12, 41, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[12, 50, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[12, 53, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[12, 49, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[12, 40, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[13, 43, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[13, 47, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[13, 55, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[13, 60, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[13, 54, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[13, 46, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[14, 44, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[14, 49, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[14, 57, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[14, 61, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[14, 56, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[14, 48, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[15, 45, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[15, 51, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[15, 59, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[15, 62, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[15, 58, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[15, 50, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[16, 52, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[16, 56, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[16, 64, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[16, 67, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[16, 63, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[16, 55, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[17, 53, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[17, 58, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[17, 66, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[17, 68, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[17, 65, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[17, 57, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"],

	[18, 61, "Hexagon::Edges::BOTTOM", "Edge::Hexagons::TOP"],
	[18, 65, "Hexagon::Edges::BOTTOM_RIGHT", "Edge::Hexagons::TOP"],
	[18, 70, "Hexagon::Edges::TOP_RIGHT", "Edge::Hexagons::BOTTOM"],
	[18, 71, "Hexagon::Edges::TOP", "Edge::Hexagons::BOTTOM"],
	[18, 69, "Hexagon::Edges::TOP_LEFT", "Edge::Hexagons::BOTTOM"],
	[18, 64, "Hexagon::Edges::BOTTOM_LEFT", "Edge::Hexagons::TOP"]

]


HexagonID = 0
EdgeID = 1
HexagonsEdgeIndex = 2
EdgesHexagonIndex = 3


with open("GameData2.json", "r") as file:
	data = json.load(file)

for relation in relationships:
	hexagon_id = relation[HexagonID]
	edge_id = relation[EdgeID]
	hexagon = next(hexagon for hexagon in data["Hexagons"] if(hexagon["id"] == hexagon_id))
	edge = next(edge for edge in data["Edges"] if(edge["id"] == edge_id))
	if("Edges" not in hexagon):
		hexagon["Edges"] = {}
	if("Hexagons" not in edge):
		edge["Hexagons"] = {}

	hexagon["Edges"][relation[HexagonsEdgeIndex]] = edge_id
	edge["Hexagons"][relation[EdgesHexagonIndex]] = hexagon_id

with open("GameData3.json", "w") as file:
	file.write(json.dumps(data, indent=4))
