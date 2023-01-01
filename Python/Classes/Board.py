


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

		self._associate_corners_edges_and_corners_hexagons(data)
		self._associate_edges_corners_and_edges_hexagons(data)
		self._associate_hexagons_corners_and_hexagons_edges(data)

		for edge in self._edges.values():
			print(edge._corners)


	def _associate_corners_edges_and_corners_hexagons(self, data: dict) -> None:
		"""
		Associates corners with their edges. As in a corner has edges that are being linked to it.
		Associates corners with their hexagons. As in a corner has hexagons that are being linked to it.
		"""
		for corner_id, corner_data in data["corners"].items():
			for corner_edge_id, edge_id in corner_data["edges"].items():
				corner = self._corners[corner_id]
				edge = self._edges[edge_id]
				corner._edges[corner_edge_id] = edge

			for corner_hexagon_id, hexagon_id in corner_data["hexagons"].items():
				corner = self._corners[corner_id]
				hexagon = self._hexagons[hexagon_id]
				corner._hexagons[corner_hexagon_id] = hexagon


	def _associate_edges_corners_and_edges_hexagons(self, data: dict) -> None:
		"""
		Associates edges with their corners. As in a edge has corners that are being linked to it.
		Associates edges with their hexagons. As in a edge has hexagons that are being linked to it.
		"""
		for edge_id, edge_data in data["edges"].items():
			for edge_corner_id, corner_id in edge_data["corners"].items():
				corner = self._corners[corner_id]
				edge = self._edges[edge_id]
				edge._corners[edge_corner_id] = corner

			for edge_hexagon_id, hexagon_id in edge_data["hexagons"].items():
				edge = self._edges[edge_id]
				hexagon = self._hexagons[hexagon_id]
				edge._hexagons[edge_hexagon_id] = hexagon


	def _associate_hexagons_corners_and_hexagons_edges(self, data: dict) -> None:
		"""
		Associates hexagons with their corners. As in a hexagon has corners that are being linked to it.
		Associates hexagons with their edges. As in a hexagon has edges that are being linked to it.
		"""
		for hexagon_id, hexagon_data in data["hexagons"].items():
			for hexagon_corner_id, corner_id in hexagon_data["corners"].items():
				corner = self._corners[corner_id]
				hexagon = self._hexagons[hexagon_id]
				hexagon._corners[hexagon_corner_id] = corner

			for hexagon_edge_id, edge_id in hexagon_data["edges"].items():
				edge = self._edges[edge_id]
				hexagon = self._hexagons[hexagon_id]
				hexagon._edges[hexagon_edge_id] = edge


	def _create_corners(self, corner_data: dict) -> None:
		[self._corners.update({corner_id: Corner(corner_id)}) for corner_id in corner_data.keys()]


	def _create_edges(self, edge_data: dict) -> None:
		[self._edges.update({id: Edge(id)}) for id in edge_data]


	def _create_hexagons(self, hexagon_data: dict) -> None:
		[self._hexagons.update({id: Hexagon(id, data["type"], data["value"])}) for id, data in hexagon_data.items()]
