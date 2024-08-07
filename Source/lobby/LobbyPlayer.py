

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


	def __eq__(self, right: int | str | LobbyPlayer) -> bool:
		if(isinstance(right, LobbyPlayer)):
			return self.id == right.id

		if(isinstance(right, str)):
			return self.uuid == right

		if(isinstance(right, int)):
			return self.id == right

		raise TypeError(f"LobbyPlayer.__eq__ expects type int | str | LobbyPlayer, not {type(right).__name__}")


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"uuid": self.uuid,
			"created": self.created,
			"updated": self.updated,
			"expired": self.expired,
			"name": self.name,
			"color": dict(self.color)
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4)


	def update(self) -> None:
		self.updated = datetime.now()
