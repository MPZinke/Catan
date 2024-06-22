

from datetime import datetime
from typing import Optional


DictList = list[dict]


class GameData:
	def __init__(self, id: Optional[datetime.datetime]=None, started: Optional[datetime.datetime]=None,
		finished: Optional[datetime.datetime]=None, board_id: Optional[datetime.datetime]=None,
		ports: Optional[DictList]=None, roads: Optional[DictList]=None, robber: Optional[dict]=None,
		settlements: Optional[DictList]=None, tiles: Optional[DictList]=None
	):
		self._id: Optional[int] = None
		self._started: Optional[datetime.datetime] = None
		self._finished: Optional[datetime.datetime] = None
		self._board_id: Optional[int] = None
		self._ports: Optional[DictList] = None
		self._roads: Optional[DictList] = None
		self._robber: Optional[DictList] = None
		self._settlements: Optional[DictList] = None
		self._tiles: Optional[DictList] = None

		self.id: Optional[int] = id
		self.started: Optional[datetime.datetime] = started
		self.finished: Optional[datetime.datetime] = finished
		self.board_id: Optional[int] = board_id
		self.ports: Optional[DictList] = ports
		self.roads: Optional[DictList] = roads
		self.robber: Optional[DictList] = robber
		self.settlements: Optional[DictList] = settlements
		self.tiles: Optional[DictList] = tiles


	@property
	def id(self) -> Optional[int]:
		return self._id


	@id.setter
	def id(self, new_id: Optional[int]) -> None:
		if(new_id is not None):
			self._id = new_id


	@property
	def started(self) -> Optional[datetime.datetime]:
		return self._started


	@started.setter
	def started(self, new_started: Optional[datetime.datetime]) -> None:
		if(new_started is not None):
			self._started = new_started


	@property
	def finished(self) -> Optional[datetime.datetime]:
		return self._finished


	@finished.setter
	def finished(self, new_finished: Optional[DictList]) -> datetime.datetime:
		if(new_finished is not None):
			self._finished = new_finished


	@property
	def board_id(self) -> Optional[int]:
		return self._board_id


	@board_id.setter
	def board_id(self, new_board_id: Optional[int]) -> None:
		if(new_board_id is not None):
			self._board_id = new_board_id


	@property
	def ports(self) -> Optional[DictList]:
		return self._ports


	@ports.setter
	def ports(self, new_ports: Optional[DictList]) -> None:
		if(new_ports is not None):
			self._ports = new_ports


	@property
	def roads(self) -> Optional[DictList]:
		return self._roads


	@roads.setter
	def roads(self, new_roads: Optional[DictList]) -> None:
		if(new_roads is not None):
			self._roads = new_roads


	@property
	def robber(self) -> Optional[DictList]:
		return self._robber


	@robber.setter
	def robber(self, new_robber: Optional[DictList]) -> None:
		if(new_robber is not None):
			self._robber = new_robber


	@property
	def settlements(self) -> Optional[DictList]:
		return self._settlements


	@settlements.setter
	def settlements(self, new_settlements: Optional[DictList]) -> None:
		if(new_settlements is not None):
			self._settlements = new_settlements


	@property
	def tiles(self) -> Optional[DictList]:
		return self._tiles


	@tiles.setter
	def tiles(self, new_tiles: Optional[DictList]) -> None:
		if(new_tiles is not None):
			self._tiles = new_tiles
