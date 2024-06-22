

from board import Board, 
from game import Player, Players


class Game:
	def __init__(self, id: int, board: Board, players: list[Player]):
		self.id: int = id
		self.board: Board = board
		self.players: list[Players] = players
		self.resources: list[int] = []
