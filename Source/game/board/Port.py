

from typing import Optional, TypeVar


from database.queries import directions, types
from Enum import Enum


Port = TypeVar("Port")
Ports = list[Port]
Settlement = TypeVar("Settlement")
Settlements = list[Optional[Settlement]]


class Port:
	Settlements = Enum("Port::Settlements", **{type["label"]: type["id"]-1 for type in directions.get_side_corners()})
	ResourceTypes = Enum("Tile::ResourceTypes", **{type["label"]: type["id"]-1 for type in types.get_resource_types()})

	def __init__(self, id: str, type: int):
		self.id: int = id
		self.type: int = type

		self.settlements: Settlements = [None for _ in range(self.Settlements.length)]


	def __eq__(self, right: Port) -> bool:
		return self.id == right.id