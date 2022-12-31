

class Board:
	def __init__(self, data: dict):
		self._hexagons = {}
		self._edges = {}
		self._corners = {}
		self._ports = {}
		self._players = {}
		
	def _determine_hexagons(data: dict) -> None:
		for id, hexagon_info in data["hexagons"].items():
			self._hexagons[id] = Hexagon(hexagon_info["id"], hexagon_info["type"])


