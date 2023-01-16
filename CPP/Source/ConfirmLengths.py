

import json


with open("GameData4.json", "r") as file:
	data = json.load(file)


def compareAB(A, B):
	a_b = []
	b_a = []
	a_b_count = 0
	b_a_count = 0

	for a in data[A]:
		a_b_count += len(a[B])
		for b in a[B]:
			a_b.append(f"""{a["id"]}-{a[B][b]}""")

	for b in data[B]:
		b_a_count += len(b[A])
		for a in b[A]:
			b_a.append(f"""{b[A][a]}-{b["id"]}""")

	for ab in a_b:
		if(ab not in b_a):
			print(f"{A}{B} [{A}-{B}] missing {ab}")
	for ba in b_a:
		if(ba not in a_b):
			print(f"{B}{A} [{A}-{B}] missing {ba}")

	assert(a_b_count == b_a_count)
	return a_b_count

# edge_corner_count = 0
# edge_corner = []
# corner_edge_count = 0
# corner_edge = []
# for corner in data["Corners"]:
# 	edge_corner_count += len(corner["Edges"])
# 	for edge in corner["Edges"]:
# 		edge_corner.append(f"""{corner["id"]}-{corner["Edges"][edge]}""")

# for edge in data["Edges"]:
# 	corner_edge_count += len(edge["Corners"])
# 	for corner in edge["Corners"]:
# 		corner_edge.append(f"""{edge["Corners"][corner]}-{edge["id"]}""")

# for ce in corner_edge:
# 	if(ce not in edge_corner):
# 		print(f"Corner Edge {ce}")

# for ec in edge_corner:
# 	if(ec not in corner_edge):
# 		print(f"Edge Corner {ec}")


assert(compareAB("Corners", "Edges") == 144)
assert(compareAB("Hexagons", "Edges") == 114)
assert(compareAB("Hexagons", "Corners") == 114)


# assert(corner_edge_count == edge_corner_count), f"{corner_edge_count} != {edge_corner_count}"
# assert(corner_edge_count == 144)
