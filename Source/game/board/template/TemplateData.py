

from typing import Tuple


DictList = list[dict]


class TemplateData:
	def __init__(self, *,
		id: int,
		size: Tuple[int, int],
		name: str,
		ports: DictList,
		roads: DictList,
		settlements: DictList,
		tiles: DictList
	):
		self.id: int = id
		self.size: Tuple[int, int] = size
		self.name: str = name
		self.ports: DictList = ports
		self.roads: DictList = roads
		self.settlements: DictList = settlements
		self.tiles: DictList = tiles
	