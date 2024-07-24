

from datetime import datetime
import json
from typing import TypeVar


LobbyPlayer = TypeVar("LobbyPlayer")
PlayerColor = TypeVar("PlayerColor")


class LobbyPlayer:
	def __init__(self, id: int, uuid: str, created: datetime, updated: datetime, expired: bool, name: str,
		color: PlayerColor
	):
		self.id: int = id
		self.uuid: str = uuid
		self.created: datetime = created
		self.updated: datetime = updated
		self.expired: bool = expired
		self.name: str = name
		self.color: PlayerColor = color


	def __eq__(self, right: str | LobbyPlayer) -> bool:
		if(isinstance(right, LobbyPlayer)):
			return self.id == right.id

		if(isinstance(right, str)):
			return self.id == right

		raise TypeError(f"LobbyPlayer.__eq__ expects type uuid|LobbyPlayer, not {type(right).__name__}")


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"name": self.name,
			"color": list(self.color),
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4)


	def update(self) -> None:
		self.updated = datetime.now()
