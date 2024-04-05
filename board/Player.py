

from typing import TypeVar


Player = TypeVar("Player")
Port = TypeVar("Port")
Road = TypeVar("Road")
Settlement = TypeVar("Settlement")


class Player:
	def __init__(self, id: int):
		self.id: int = id

		self.roads: list[Road] = []
		self.settlements: list[Settlement] = []


	def __eq__(self, right: Player) -> bool:
		return self.id == right.id


	def ports(self) -> list[Port]:
		found_ports: list[Port] = []
		for settlement in self.settlements:
			for port in settlement.ports:
				if(port not in found_ports):
					found_ports.append(port)

		return found_ports
