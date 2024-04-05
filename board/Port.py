

from typing import TypeVar


from board.Tile import Tile
from ResourceType import ResourceType


Port = TypeVar("Port")


class Port:
	Settlements = Tile.Settlements
	Types = type("ResourceType", ResourceType.__bases__,
		{
			**ResourceType.__dict__,
			"__annotations__": {**ResourceType.__annotations__, "ANY": int}
		}
	)

	def __init__(self, id: str, type: int):
		self.id: int = id
		self.type: int = type

		self.settlements: list = [None for _ in range(self.Settlements.length)]


	def __eq__(self, right: Port) -> bool:
		return self.id == right.id
