

import json


relationships = [
	[0, 0, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[0, 1, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[1, 0, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[1, 2, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[2, 3, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[2, 5, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[3, 1, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[3, 3, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[3, 6, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[4, 2, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[4, 4, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[4, 7, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[5, 4, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[5, 8, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[6, 9, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[6, 12, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[7, 5, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[7, 9, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[7, 13, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[8, 6, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[8, 10, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[8, 14, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[9, 7, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[9, 10, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[9, 15, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[10, 8, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[10, 11, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[10, 16, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[11, 11, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[11, 17, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[12, 12, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[12, 20, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[13, 13, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[13, 18, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[13, 21, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[14, 14, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[14, 18, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[14, 22, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[15, 15, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[15, 19, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[15, 23, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[16, 16, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[16, 19, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[16, 24, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[17, 17, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[17, 25, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[18, 20, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[18, 26, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[18, 29, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[19, 21, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[19, 26, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[19, 30, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[20, 22, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[20, 27, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[20, 31, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[21, 23, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[21, 27, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[21, 32, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[22, 24, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[22, 28, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[22, 33, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[23, 25, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[23, 28, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[23, 34, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[24, 29, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[24, 37, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[25, 30, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[25, 35, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[25, 38, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[26, 31, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[26, 35, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[26, 39, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[27, 32, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[27, 36, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[27, 40, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[28, 33, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[28, 36, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[28, 41, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[29, 34, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[29, 42, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[30, 37, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[30, 43, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[30, 46, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[31, 38, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[31, 43, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[31, 47, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[32, 39, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[32, 44, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[32, 48, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[33, 40, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[33, 44, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[33, 49, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[34, 41, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[34, 45, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[34, 50, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[35, 42, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[35, 45, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[35, 51, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[36, 46, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[36, 54, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[37, 47, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[37, 52, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[37, 55, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[38, 48, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[38, 52, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[38, 56, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[39, 49, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[39, 53, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[39, 57, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[40, 50, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[40, 53, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[40, 58, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[41, 51, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[41, 59, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[42, 54, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[42, 60, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],

	[43, 55, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[43, 60, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[43, 63, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[44, 56, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[44, 61, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[44, 64, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[45, 57, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[45, 61, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[45, 65, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[46, 58, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[46, 62, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[46, 66, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[47, 59, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[47, 62, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],

	[48, 63, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[48, 67, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],

	[49, 64, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[49, 67, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],
	[49, 69, "Corner::Edges::TOP", "Edge::Corners::LEFT"],

	[50, 65, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[50, 68, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],
	[50, 70, "Corner::Edges::TOP", "Edge::Corners::RIGHT"],

	[51, 66, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[51, 68, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"],

	[52, 69, "Corner::Edges::BOTTOM", "Edge::Corners::RIGHT"],
	[52, 71, "Corner::Edges::SIDE", "Edge::Corners::LEFT"],

	[53, 70, "Corner::Edges::BOTTOM", "Edge::Corners::LEFT"],
	[53, 71, "Corner::Edges::SIDE", "Edge::Corners::RIGHT"]

]


CornerID = 0
EdgeID = 1
CornersEdgeIndex = 2
EdgesCornerIndex = 3


with open("GameData3.json", "r") as file:
	data = json.load(file)

for relation in relationships:
	corner_id = relation[CornerID]
	edge_id = relation[EdgeID]
	corner = next(corner for corner in data["Corners"] if(corner["id"] == corner_id))
	edge = next(edge for edge in data["Edges"] if(edge["id"] == edge_id))
	if("Edges" not in corner):
		corner["Edges"] = {}
	if("Corners" not in edge):
		edge["Corners"] = {}

	corner["Edges"][relation[CornersEdgeIndex]] = edge_id
	edge["Corners"][relation[EdgesCornerIndex]] = corner_id

with open("GameData4.json", "w") as file:
	file.write(json.dumps(data, indent=4))
