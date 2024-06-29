

from datetime import datetime
import json
from typing import Optional


from game.player.Player import Player, Players  # TODO
from game.board import Board


class Game:
	def __init__(self, id: int, board: Board, players: list[Player], started: Optional[datetime]=None,
		finished: Optional[datetime]=None
	):
		self.id: int = id
		self.finished: Optional[datetime] = finished
		self.started: Optional[datetime] = started
		self.board: Board = board
		self.players: list[Players] = players
		self.resources: list[int] = []


	def __iter__(self) -> dict:
		yield from {
			"id": self.id,
			"finished": self.finished,
			"started": self.started,
			"board": dict(self.board),
			"players": list(map(dict, self.players)),
			"resources": self.resources,
		}.items()


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return json.dumps(dict(self), indent=4, default=str)
