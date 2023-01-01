

from Classes.Board import Board
from Classes import Corner, Edge, Hexagon
import Drawing
from Drawing import Canvas


def draw_board(board: Board) -> None:
	canvas: Canvas = Canvas((500, 500))
	Drawing.Hexagon(board._hexagons[1], canvas, (0, 0))
	canvas.show()


def main():
	"""
	{
		"hexagons": {
			<hexagon_id>: {
				"corners": {
					<hexagon's corner>: <corner_id>,
					...
				},
				"edges": {
					<hexagon's edge>: <edge_id>,
					...
				},
				"type": <type>,
				"value": <dice roll value>
			},
			...
		},
		"corners": {
			<corner_id>: {
				"hexagons": {
					<corner's hexagon>: <hexagon_id>,
					...
				},
				"edges": {
					<corner's edge>: <edge_id>,
					...
				}
			},
			...
		},
		"edges": {
			<edge_id>: {
				"hexagons": {
					<edge's hexagon>: <hexagon_id>,
					...
				},
				"corners": {
					<edge's corner>: <corner_id>,
					...
				}
			},
			...
		}
	}
	"""
	parts = {
		"hexagons": {
			1: {
				"corners": {
					Hexagon.CORNERS.BOTTOM_LEFT: 1,
					Hexagon.CORNERS.BOTTOM_RIGHT: 2,
					Hexagon.CORNERS.RIGHT: 3,
					Hexagon.CORNERS.TOP_RIGHT: 4,
					Hexagon.CORNERS.TOP_LEFT: 5,
					Hexagon.CORNERS.LEFT: 6
				},
				"edges": {
					Hexagon.EDGES.BOTTOM: 1,
					Hexagon.EDGES.BOTTOM_RIGHT: 2,
					Hexagon.EDGES.TOP_RIGHT: 3,
					Hexagon.EDGES.TOP: 4,
					Hexagon.EDGES.TOP_LEFT: 5,
					Hexagon.EDGES.BOTTOM_LEFT: 6
				},
				"type": "DESSERT",
				"value": 6
			}
		},
		"corners": {
			1: {
				"hexagons": {
					Corner.HEXAGONS.TOP: 1
				},
				"edges": {
					Corner.EDGES.TOP: 6,
					Corner.EDGES.SIDE: 1
				}
			},
			2: {
				"hexagons": {
					Corner.HEXAGONS.TOP: 1
				},
				"edges": {
					Corner.EDGES.SIDE: 1,
					Corner.EDGES.TOP: 2
				}
			},
			3: {
				"hexagons": {
					Corner.HEXAGONS.SIDE: 1
				},
				"edges": {
					Corner.EDGES.BOTTOM: 2,
					Corner.EDGES.TOP: 3
				}
			},
			4: {
				"hexagons": {
					Corner.HEXAGONS.BOTTOM: 1
				},
				"edges": {
					Corner.EDGES.BOTTOM: 3,
					Corner.EDGES.SIDE: 4
				}
			},
			5: {
				"hexagons": {
					Corner.HEXAGONS.BOTTOM: 1
				},
				"edges": {
					Corner.EDGES.BOTTOM: 5,
					Corner.EDGES.SIDE: 4
				}
			},
			6: {
				"hexagons": {
					Corner.HEXAGONS.SIDE: 1
				},
				"edges": {
					Corner.EDGES.BOTTOM: 6,
					Corner.EDGES.TOP: 5
				}
			}
		},
		"edges": {
			1: {
				"corners": {
					Edge.CORNERS.LEFT: 1,
					Edge.CORNERS.RIGHT: 2
				},
				"hexagons": {
					Edge.HEXAGONS.TOP: 1
				}
			},
			2: {
				"corners": {
					Edge.CORNERS.LEFT: 2,
					Edge.CORNERS.RIGHT: 3
				},
				"hexagons": {
					Edge.HEXAGONS.TOP: 1
				}
			},
			3: {
				"corners": {
					Edge.CORNERS.LEFT: 4,
					Edge.CORNERS.RIGHT: 3
				},
				"hexagons": {
					Edge.HEXAGONS.BOTTOM: 1
				}
			},
			4: {
				"corners": {
					Edge.CORNERS.LEFT: 5,
					Edge.CORNERS.RIGHT: 4
				},
				"hexagons": {
					Edge.HEXAGONS.BOTTOM: 1
				}
			},
			5: {
				"corners": {
					Edge.CORNERS.LEFT: 6,
					Edge.CORNERS.RIGHT: 5
				},
				"hexagons": {
					Edge.HEXAGONS.BOTTOM: 1
				}
			},
			6: {
				"corners": {
					Edge.CORNERS.LEFT: 6,
					Edge.CORNERS.RIGHT: 1
				},
				"hexagons": {
					Edge.HEXAGONS.TOP: 1
				}
			}
		}
	}

	board = Board(parts)

	print(board)
	print()
	draw_board(board)


if(__name__ == "__main__"):
	main()
