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


from PlayerColor import PlayerColor, PLAYER_COLORS


Lobby = TypeVar("Lobby")
LobbyPlayer = TypeVar("LobbyPlayer")


class Lobby:
	def __init__(self, id: int, uuid: str, created: datetime, updated: datetime, expired: bool,
		players: Optional[list[LobbyPlayer]]=None, game_id: Optional[int]=None
	):
		self.id: str = id
		self.uuid: str = uuid
		self.created: datetime = created
		self.updated: datetime = updated
		self.expired: bool = expired
		self.players: list[LobbyPlayer] = list(players) if(players is not None) else []
		self.game_id: Optional[int] = game_id


	def __eq__(self, right: str | Lobby) -> bool:
		if(isinstance(right, Lobby)):
			return self.id == right.id

		if(isinstance(right, str)):
			return self.uuid == right

		if(isinstance(right, int)):
			return self.id == right

		raise TypeError(f"Lobby.__eq__ expects type int | str | Lobby, not {type(right).__name__}")


	def __iadd__(self, player: LobbyPlayer) -> Lobby:
		if(player.id in self.players):
			raise Exception("A player with that ID already exists")

		self.players.append(player)
		return self


	def __contains__(self, left: str | LobbyPlayer) -> bool:
		return left in self.players


	def __len__(self) -> int:
		return len(self.players)


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"uuid": self.uuid,
			"created": self.created,
			"updated": self.updated,
			"expired": self.expired,
			"players": list(map(dict, self.players)),
			"game_id": self.game_id
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), default=str, indent=4)


	def available_player_colors(self) -> list[PlayerColor]:
		player_color_ids = [player.color.id for player in self.players]
		return [player_color for player_color in PLAYER_COLORS if(player_color.id not in player_color_ids)]


	def get(self, player_id) -> Optional[LobbyPlayer]:
		for player in self.players:
			if(player == player_id):
				return player

		return None		
