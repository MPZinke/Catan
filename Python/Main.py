

import math


from Classes.Board import Board
from Classes import Corner, Edge, Hexagon
import Drawing
from Drawing import Canvas
import Parts


def draw_hexagon(canvas, hexagon, position, visited_hexagon_ids) -> None:
	Drawing.Hexagon(hexagon, canvas, position)
	print(f"Drawing hexagon: {hexagon._id} type {hexagon._type} position {position}")
	visited_hexagon_ids.append(hexagon._id)
	edge_ids = Hexagon.EDGES
	for edge_id in [edge_ids.BOTTOM, edge_ids.BOTTOM_RIGHT, edge_ids.TOP_RIGHT, edge_ids.TOP, edge_ids.TOP_LEFT, edge_ids.BOTTOM_LEFT]:
		edge = hexagon._edges[edge_id]
		if(edge is None):
			continue

		opposing_hexagon = edge ^ hexagon
		if(opposing_hexagon is not None and opposing_hexagon._id not in visited_hexagon_ids):
			if(edge_id == edge_ids.BOTTOM):
				next_position = (position[0], position[1] - 103)
			if(edge_id == edge_ids.TOP):
				next_position = (position[0], position[1] + 103)
			if(edge_id == edge_ids.BOTTOM_RIGHT):
				next_position = (
				  position[0] + 60 + 60 * math.cos(60 * math.pi / 180.0),
				  position[1] - 60 * math.sin(60 * math.pi / 180.0)
				)
			if(edge_id == edge_ids.BOTTOM_LEFT):
				next_position = (
				  position[0] - 60 - 60 * math.cos(60 * math.pi / 180.0),
				  position[1] - 60 * math.sin(60 * math.pi / 180.0)
				)
			if(edge_id == edge_ids.TOP_RIGHT):
				next_position = (
				  position[0] + 60 + 60 * math.cos(60 * math.pi / 180.0),
				  position[1] + 60 * math.sin(60 * math.pi / 180.0)
				)
			if(edge_id == edge_ids.TOP_LEFT):
				next_position = (
				  position[0] + 60 + 60 * math.cos(60 * math.pi / 180.0),
				  position[1] + 60 * math.sin(60 * math.pi / 180.0)
				)

			draw_hexagon(canvas, opposing_hexagon, next_position, visited_hexagon_ids)



def draw_board(board: Board) -> None:
	visited_hexagon_ids: list[int] = []
	canvas: Canvas = Canvas((500, 500))
	draw_hexagon(canvas, board._hexagons[1], (250, 250), visited_hexagon_ids)
	canvas.show()


def main():
	board = Board(Parts.PARTS)

	print(board)
	print()
	draw_board(board)


if(__name__ == "__main__"):
	main()
