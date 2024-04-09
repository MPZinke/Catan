

from typing import TypeVar


from database.queries import directions
from Enum import Enum
from ResourceType import ResourceType


Port = TypeVar("Port")


class Port:
	Settlements = Enum("Port::Settlements", **{type["label"]: type["id"]-1 for type in directions.get_side_corners()})
	Types = ResourceType

	def __init__(self, id: str, type: int):
		self.id: int = id
		self.type: int = type

		self.settlements: list = [None for _ in range(self.Settlements.length)]


	def __eq__(self, right: Port) -> bool:
		return self.id == right.id
