

from datetime import datetime
from typing import Optional


from game.player.Player import Player, Players  # TODO
from game.board import Board


class Game:
	def __init__(self, id: int, board: Board, players: list[Player]):
		self.id: int = id
		self.finished: Optional[datetime]=None
		self.started: Optional[datetime]=None
		self.board: Board = board
		self.players: list[Players] = players
		self.resources: list[int] = []
