

DictList = list[dict]


class BoardTemplateData:
	def __init__(self, id: int, name: str, ports: DictList, roads: DictList, settlements: DictList,
		tiles: DictList
	):
		self.id: int = id
		self.name: str = name
		self.ports: DictList = ports
		self.roads: DictList = roads
		self.settlements: DictList = settlements
		self.tiles: DictList = tiles
