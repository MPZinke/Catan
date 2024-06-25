

from typing import TypeVar


from database.queries.types import get_resource_types
from Enum import Enum


Player = TypeVar("Player")
Players = list[Player]
Port = TypeVar("Port")
Ports = list[Port]
Road = TypeVar("Road")
Roads = list[Road]
Settlement = TypeVar("Settlement")
Settlements = list[Settlement]


class Player:
	ResourcesTypes = Enum("Player::ResourceType", **{type["label"]: type["id"]-1 for type in get_resource_types()})

	def __init__(self, id: int, name: str):
		self.id: int = id
		self.name: str = name

		self.development_cards = []
		self.resources = []  # TODO
		self.roads: Roads = []
		self.settlements: Settlements = []


	def __eq__(self, right: Player) -> bool:
		return self.id == right.id


	def ports(self) -> list[Port]:
		found_ports: list[Port] = []
		for settlement in self.settlements:
			for port in settlement.ports:
				if(port not in found_ports):
					found_ports.append(port)

		return found_ports
