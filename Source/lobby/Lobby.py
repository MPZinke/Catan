#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.07.23                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from datetime import datetime
import json
from typing import Optional, TypeVar


Lobby = TypeVar("Lobby")
LobbyPlayer = TypeVar("LobbyPlayer")


class Lobby:
	def __init__(self, id: int, uuid: str, created: datetime, updated: datetime, expired: bool,
		players: Optional[list[LobbyPlayer]]=None
	):
		self.id: str = id
		self.uuid: str = uuid
		self.created: datetime = created
		self.updated: datetime = updated
		self.expired: bool = expired
		self.players: list[LobbyPlayer] = list(players) if(players is not None) else []


	def __eq__(self, right: str | Lobby) -> bool:
		if(isinstance(right, str)):
			return self.id == right

		if(isinstance(right, Lobby)):
			return self.id == right.id

		raise TypeError(f"Lobby.__eq__ expects type str | Lobby, not {type(right).__name__}")


	def __iadd__(self, player: LobbyPlayer) -> Lobby:
		if(player.id in self.players):
			raise Exception("A player with that ID already exists")

		self.players.append(player)
		return self


	def __contains__(self, left: str | LobbyPlayer) -> bool:
		return left in self.players


	def __delitem__(self, player_id: str | LobbyPlayer) -> None:
		if(not isinstance(player_id, (str, LobbyPlayer))):
			raise TypeError(f"`player_id` must be of type `str | LobbyPlayer`, not {type(player_id)}")

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
