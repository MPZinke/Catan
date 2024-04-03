

from board import Border
from board import Corner
from board import Tile


def find(id: int) -> callable:
	def callback(item: object) -> bool:
		return item.id == id

	return callback


def borders_with_corners(border_dicts: list[dict], borders: list[Border], corners: list[Corner]):
	for border_dict in border_dicts:
		border = next(filter(find(border_dict["id"]), borders))
		for corner_direction, corner_id in border_dict["Corners"].items():
			corner = next(filter(find(corner_id), corners))
			direction_index = getattr(Border.Corners, corner_direction.split("::")[2])
			border.corners[direction_index] = corner


def borders_with_tiles(border_dicts: list[dict], borders: list[Border], tiles: list[Tile]):
	for border_dict in border_dicts:
		border = next(filter(find(border_dict["id"]), borders))
		for tile_direction, tile_id in border_dict["Tiles"].items():
			tile = next(filter(find(tile_id), tiles))
			direction_index = getattr(Border.Tiles, tile_direction.split("::")[2])
			border.tiles[direction_index] = tile


def corners_with_borders(corner_dicts: list[dict], corners: list[Corner], borders: list[Border]):
	for corner_dict in corner_dicts:
		corner = next(filter(find(corner_dict["id"]), corners))
		for border_direction, border_id in corner_dict["Borders"].items():
			border = next(filter(find(border_id), borders))
			direction_index = getattr(Corner.Borders, border_direction.split("::")[2])
			corner.borders[direction_index] = border


def corners_with_tiles(corner_dicts: list[dict], corners: list[Corner], tiles: list[Corner]):
	for corner_dict in corner_dicts:
		corner = next(filter(find(corner_dict["id"]), corners))
		for tile_direction, tile_id in corner_dict["Tiles"].items():
			tile = next(filter(find(tile_id), tiles))
			direction_index = getattr(Corner.Tiles, tile_direction.split("::")[2])
			corner.tiles[direction_index] = tile


def tiles_with_borders(tile_dicts: list[dict], tiles: list[Tile], borders: list[Border]):
	for tile_dict in tile_dicts:
		tile = next(filter(find(tile_dict["id"]), tiles))
		for border_direction, border_id in tile_dict["Borders"].items():
			border = next(filter(find(border_id), borders))
			direction_index = getattr(Tile.Borders, border_direction.split("::")[2])
			tile.borders[direction_index] = border


def tiles_with_corners(tile_dicts: list[dict], tiles: list[Border], corners: list[Corner]):
	for tile_dict in tile_dicts:
		tile = next(filter(find(tile_dict["id"]), tiles))
		for corner_direction, corner_id in tile_dict["Corners"].items():
			corner = next(filter(find(corner_id), corners))
			direction_index = getattr(Tile.Corners, corner_direction.split("::")[2])
			tile.corners[direction_index] = corner
