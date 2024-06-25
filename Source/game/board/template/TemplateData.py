

DictList = list[dict]


class TemplateData:
	def __init__(self, *,
		id: int,
		name: str,
		ports: DictList,
		roads: DictList,
		settlements: DictList,
		tiles: DictList,
		ports_settlements: DictList,
		roads_settlements: DictList,
		roads_tiles: DictList,
		settlements_tiles: DictList
	):
		self.id: int = id
		self.name: str = name
		self.ports: DictList = ports
		self.roads: DictList = roads
		self.settlements: DictList = settlements
		self.tiles: DictList = tiles
		self.ports_settlements: DictList = ports_settlements
		self.roads_settlements: DictList = roads_settlements
		self.roads_tiles: DictList = roads_tiles
		self.settlements_tiles: DictList = settlements_tiles
	