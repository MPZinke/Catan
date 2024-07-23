

from datetime import datetime, timedelta
import json
from typing import Optional, TypeVar


Color = TypeVar("Color")
LobbyPlayer = TypeVar("LobbyPlayer")
Lobby = TypeVar("Lobby")
Lobbies = TypeVar("Lobbies")


class Color:
	def __init__(self, red: int, green: int, blue: int, label: str=""):
		self.label: str = label
		self.red: str = int(max(0, min(255, red)))
		self.green: str = int(max(0, min(255, green)))
		self.blue: str = int(max(0, min(255, blue)))


	def __iter__(self) -> list[int]:
		yield from [self.red, self.green, self.blue]


	def __eq__(self, right: Color | list[int]):
		if(isinstance(right, Color)):
			return list(self) == list(right)

		if(isinstance(right, list)):
			return list(self) == right


	def hex(self) -> str:
		return f"{hex(self.red)[2:]}{hex(self.green)[2:]}{hex(self.blue)[2:]}"


class LobbyPlayer:
	COLORS = [
		Color(206, 156, 198, "Pink"),
		Color(88, 193, 98, "Green"),
		Color(48, 110, 178, "Blue"),
		Color(245, 196, 67, "Yellow"),
		Color(214, 75, 70, "Red"),
		Color(83, 53, 68, "Purple"),
	]

	def __init__(self, id: str, name: str, color: Color):
		self.id: str = id
		self.created: datetime = datetime.now()
		self.last_updated: datetime = self.created
		self.name: str = name
		self.color: Color = color


	def __eq__(self, right: str|LobbyPlayer) -> bool:
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
		self.last_updated = datetime.now()


class Lobby:
	def __init__(self, id: str, *players: list[LobbyPlayer]):
		self.id: str = id
		self.created: datetime = datetime.now()
		self.last_updated: datetime = self.created
		self.players: list[LobbyPlayer] = list(players)


	def __eq__(self, right: str|Lobby) -> bool:
		if(isinstance(right, str)):
			return self.id == right

		if(isinstance(right, Lobby)):
			return self.id == right.id

		raise TypeError(f"Lobby.__eq__ expects type str|Lobby, not {type(right).__name__}")


	def __iadd__(self, player: LobbyPlayer) -> Lobby:
		if(player.id in self.players):
			raise Exception("A player with that ID already exists")

		self.players.append(player)
		return self


	def __contains__(self, left: str|LobbyPlayer) -> bool:
		return left in self.players


	def __delitem__(self, player_id: str|LobbyPlayer) -> None:
		if(not isinstance(player_id, (str, LobbyPlayer))):
			raise TypeError(f"`player_id` must be of type `str|LobbyPlayer`, not {type(player_id)}")

		if(isinstance(player_id, LobbyPlayer)):
			player_id = player_id.id

		for index in range(len(self.players)-1, -1, -1):
			if(self.players[index].id == player_id):
				del self.players[index]


	def __getitem__(self, player_id: str) -> Lobby:
		player: Optional[LobbyPlayer] = self.get(player_id)
		if(player is None):
			raise IndexError(f"LobbyPlayer with id '{player_id}' not found.")

		return player


	def __len__(self) -> int:
		return len(self.players)


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"created": self.created,
			"players": list(map(dict, self.players)),
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), default=str, indent=4)


	def get(self, player_id) -> Optional[LobbyPlayer]:
		for player in self.players:
			if(player == player_id):
				return player

		return None		


	def update(self) -> None:
		self.last_updated = datetime.now()


class Lobbies:
	def __init__(self):
		self.lobbies = []


	def __iadd__(self, lobby: Lobby) -> Lobbies:
		self.remove_stale_lobbies()

		if(lobby in self.lobbies):
			raise Exception("A lobby with that ID already exists")

		self.lobbies.append(lobby)
		return self


	def __contains__(self, left: str|Lobby) -> bool:
		return left in self.lobbies


	def __delitem__(self, lobby_id: str|Lobby) -> None:
		if(not isinstance(lobby_id, (str, Lobby))):
			raise TypeError(f"`lobby_id` must be of type `str|Lobby`, not {type(lobby_id)}")

		if(isinstance(lobby_id, Lobby)):
			lobby_id = lobby_id.id

		for index in range(len(self.lobbies)-1, -1, -1):
			if(self.lobbies[index].id == lobby_id):
				del self.lobbies[index]


	def __getitem__(self, lobby_id: str) -> Lobby:
		lobby: Optional[Lobby] = self.get(lobby_id)
		if(lobby is None):
			raise IndexError(f"LobbyPlayer with id '{lobby_id}' not found.")


		raise ValueError(f"Lobby with id '{lobby_id}' not found.")


	def __len__(self) -> int:
		return len(self.lobbies)


	def __iter__(self) -> dict:
		yield from list(map(dict, self.lobbies))


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(list(self), default=str, indent=4)


	def append(self, lobby: Lobby) -> None:
		self += lobby


	def get(self, lobby_id) -> Optional[Lobby]:
		for lobby in self.lobbies:
			if(lobby == lobby_id):
				return lobby

		return None


	def remove_stale_lobbies(self) -> None:
		now: datetime = datetime.now()
		for x in range(len(self.lobbies)-1, -1, -1):
			if(now < self.lobbies[x].created + timedelta(hours=2)):
				self.lobbies.pop(x)
