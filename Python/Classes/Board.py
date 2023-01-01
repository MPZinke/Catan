


from Classes import Corner, Edge, Hexagon


class Board:
	def __init__(self, data: dict):
		self._hexagons = {}
		self._edges = {}
		self._corners = {}
		self._ports = {}
		self._players = {}

		self._create_corners(data["corners"])
		self._create_edges(data["edges"])
		self._create_hexagons(data["hexagons"])

		self._associate_corners(data)


	def _associate_corners(self, data: dict) -> None:
		for hexagon_id, hexagon_data in data["hexagons"].items():
			for hexagon_corner, corner_id in hexagon_data["corners"]:
				corner = self._corners[corner_id]
				hexagon = self._hexagons[hexagon_id]
				self._hexagons[hexagon_id]._corners[hexagon_corner] = corner
				if(hexagon_corner in [Corner.BOTTOM_LEFT, Corner.BOTTOM_RIGHT]):
					corner.top = hexagon
				elif(hexagon_corner in [Corner.RIGHT, Corner.LEFT]):
					corner.side = hexagon
				else:
					corner.bottom = hexagon


	def _create_corners(self, corner_data: dict) -> None:
		[self._corners.update({id: Corner(id)}) for hexagon_corner, corner_id in corner_data.items()]


	def _create_edges(self, edge_data: dict) -> None:
		[self._edges.update({id: Edge(id)}) for id in edge_data]


	def _create_hexagons(self, hexagon_data: dict) -> None:
		[self._hexagons.update({id: Hexagon(id, data["type"], data["value"])}) for id, data in hexagon_data.items()]
