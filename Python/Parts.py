

from Classes import Corner, Edge, Hexagon


"""
{
	"hexagons": {
		<hexagon_id>: {
			"corners": {<hexagon's corner>: <corner_id>, ...},
			"edges": {<hexagon's edge>: <edge_id>, ...},
			"type": <type>,
			"value": <dice roll value>
		},
		...
	},
	"corners": {
		<corner_id>: {
			"hexagons": {<corner's hexagon>: <hexagon_id>, ...},
			"edges": {<corner's edge>: <edge_id>, ...}
		},
		...
	},
	"edges": {
		<edge_id>: {
			"hexagons": {<edge's hexagon>: <hexagon_id>, ...},
			"corners": {<edge's corner>: <corner_id>, ...}
		},
		...
	}
}
"""
PARTS = {
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
			"type": Hexagon.DESSERT,
			"value": 0
		},
		2: {
			"corners": {
				Hexagon.CORNERS.BOTTOM_LEFT: 5,
				Hexagon.CORNERS.BOTTOM_RIGHT: 4,
				Hexagon.CORNERS.RIGHT: 7,
				Hexagon.CORNERS.TOP_RIGHT: 8,
				Hexagon.CORNERS.TOP_LEFT: 9,
				Hexagon.CORNERS.LEFT: 10
			},
			"edges": {
				Hexagon.EDGES.BOTTOM: 4,
				Hexagon.EDGES.BOTTOM_RIGHT: 7,
				Hexagon.EDGES.TOP_RIGHT: 8,
				Hexagon.EDGES.TOP: 9,
				Hexagon.EDGES.TOP_LEFT: 10,
				Hexagon.EDGES.BOTTOM_LEFT: 11
			},
			"type": Hexagon.STONE,
			"value": 6
		},
		3: {
			"corners": {
				Hexagon.CORNERS.BOTTOM_LEFT: 13,
				Hexagon.CORNERS.BOTTOM_RIGHT: 6,
				Hexagon.CORNERS.RIGHT: 5,
				Hexagon.CORNERS.TOP_RIGHT: 10,
				Hexagon.CORNERS.TOP_LEFT: 11,
				Hexagon.CORNERS.LEFT: 12
			},
			"edges": {
				Hexagon.EDGES.BOTTOM: 15,
				Hexagon.EDGES.BOTTOM_RIGHT: 5,
				Hexagon.EDGES.TOP_RIGHT: 11,
				Hexagon.EDGES.TOP: 12,
				Hexagon.EDGES.TOP_LEFT: 13,
				Hexagon.EDGES.BOTTOM_LEFT: 14
			},
			"type": Hexagon.BRICK,
			"value": 6
		},
		4: {
			"corners": {
				Hexagon.CORNERS.BOTTOM_LEFT: 9,
				Hexagon.CORNERS.BOTTOM_RIGHT: 8,
				Hexagon.CORNERS.RIGHT: 14,
				Hexagon.CORNERS.TOP_RIGHT: 15,
				Hexagon.CORNERS.TOP_LEFT: 16,
				Hexagon.CORNERS.LEFT: 17
			},
			"edges": {
				Hexagon.EDGES.BOTTOM: 9,
				Hexagon.EDGES.BOTTOM_RIGHT: 16,
				Hexagon.EDGES.TOP_RIGHT: 17,
				Hexagon.EDGES.TOP: 18,
				Hexagon.EDGES.TOP_LEFT: 19,
				Hexagon.EDGES.BOTTOM_LEFT: 20
			},
			"type": Hexagon.TREE,
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
				Corner.HEXAGONS.BOTTOM: 1,
				Corner.HEXAGONS.TOP: 2
			},
			"edges": {
				Corner.EDGES.BOTTOM: 3,
				Corner.EDGES.SIDE: 4,
				Corner.EDGES.TOP: 7
			}
		},
		5: {
			"hexagons": {
				Corner.HEXAGONS.BOTTOM: 1,
				Corner.HEXAGONS.TOP: 2,
				Corner.HEXAGONS.SIDE: 3
			},
			"edges": {
				Corner.EDGES.BOTTOM: 5,
				Corner.EDGES.SIDE: 4,
				Corner.EDGES.TOP: 11
			}
		},
		6: {
			"hexagons": {
				Corner.HEXAGONS.SIDE: 1,
				Corner.HEXAGONS.TOP: 3
			},
			"edges": {
				Corner.EDGES.BOTTOM: 6,
				Corner.EDGES.TOP: 5,
				Corner.EDGES.SIDE: 15
			}
		},
		7: {
			"hexagons": {
				Corner.HEXAGONS.SIDE: 2
			},
			"edges": {
				Corner.EDGES.BOTTOM: 7,
				Corner.EDGES.TOP: 8
			}
		},
		8: {
			"hexagons": {
				Corner.HEXAGONS.BOTTOM: 2,
				Corner.HEXAGONS.TOP: 4,
			},
			"edges": {
				Corner.EDGES.BOTTOM: 8,
				Corner.EDGES.TOP: 16,
				Corner.EDGES.SIDE: 9
			}
		},
		9: {
			"hexagons": {
				Corner.HEXAGONS.BOTTOM: 2,
				Corner.HEXAGONS.TOP: 4,
			},
			"edges": {
				Corner.EDGES.SIDE: 9,
				Corner.EDGES.BOTTOM: 10,
				Corner.EDGES.TOP: 20
			}
		},
		10: {
			"hexagons": {
				Corner.HEXAGONS.BOTTOM: 3,
				Corner.HEXAGONS.SIDE: 2
			},
			"edges": {
				Corner.EDGES.BOTTOM: 11,
				Corner.EDGES.TOP: 10,
				Corner.EDGES.SIDE: 12
			}
		},
		11: {
			"hexagons": {
				Corner.HEXAGONS.BOTTOM: 3
			},
			"edges": {
				Corner.EDGES.BOTTOM: 13,
				Corner.EDGES.SIDE: 12
			}
		},
		12: {
			"hexagons": {
				Corner.HEXAGONS.SIDE: 3
			},
			"edges": {
				Corner.EDGES.BOTTOM: 13,
				Corner.EDGES.TOP: 14
			}
		},
		13: {
			"hexagons": {
				Corner.HEXAGONS.SIDE: 3
			},
			"edges": {
				Corner.EDGES.SIDE: 15,
				Corner.EDGES.TOP: 14
			}
		},
		14: {
			"hexagons": {
				Corner.HEXAGONS.SIDE: 4
			},
			"edges": {
				Corner.EDGES.BOTTOM: 17,
				Corner.EDGES.TOP: 16
			}
		},
		15: {
			"hexagons": {
				Corner.HEXAGONS.BOTTOM: 4
			},
			"edges": {
				Corner.EDGES.SIDE: 18,
				Corner.EDGES.BOTTOM: 17
			}
		},
		16: {
			"hexagons": {
				Corner.HEXAGONS.SIDE: 4
			},
			"edges": {
				Corner.EDGES.BOTTOM: 19,
				Corner.EDGES.SIDE: 18
			}
		},
		17: {
			"hexagons": {
				Corner.HEXAGONS.SIDE: 4
			},
			"edges": {
				Corner.EDGES.BOTTOM: 20,
				Corner.EDGES.TOP: 19
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
				Edge.HEXAGONS.BOTTOM: 1,
				Edge.HEXAGONS.TOP: 2
			}
		},
		5: {
			"corners": {
				Edge.CORNERS.LEFT: 6,
				Edge.CORNERS.RIGHT: 5
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 1,
				Edge.HEXAGONS.TOP: 3
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
		},
		7: {
			"corners": {
				Edge.CORNERS.LEFT: 4,
				Edge.CORNERS.RIGHT: 7
			},
			"hexagons": {
				Edge.HEXAGONS.TOP: 2
			}
		},
		8: {
			"corners": {
				Edge.CORNERS.LEFT: 8,
				Edge.CORNERS.RIGHT: 7
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 2
			}
		},
		9: {
			"corners": {
				Edge.CORNERS.LEFT: 9,
				Edge.CORNERS.RIGHT: 8
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 2,
				Edge.HEXAGONS.TOP: 4,
			}
		},
		10: {
			"corners": {
				Edge.CORNERS.LEFT: 10,
				Edge.CORNERS.RIGHT: 9
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 2
			}
		},
		11: {
			"corners": {
				Edge.CORNERS.LEFT: 10,
				Edge.CORNERS.RIGHT: 5
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 3,
				Edge.HEXAGONS.TOP: 2
			}
		},
		12: {
			"corners": {
				Edge.CORNERS.LEFT: 11,
				Edge.CORNERS.RIGHT: 10
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 3
			}
		},
		13: {
			"corners": {
				Edge.CORNERS.LEFT: 12,
				Edge.CORNERS.RIGHT: 11
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 3
			}
		},
		14: {
			"corners": {
				Edge.CORNERS.LEFT: 12,
				Edge.CORNERS.RIGHT: 13
			},
			"hexagons": {
				Edge.HEXAGONS.TOP: 3
			}
		},
		15: {
			"corners": {
				Edge.CORNERS.LEFT: 13,
				Edge.CORNERS.RIGHT: 6
			},
			"hexagons": {
				Edge.HEXAGONS.TOP: 3
			}
		},
		16: {
			"corners": {
				Edge.CORNERS.LEFT: 8,
				Edge.CORNERS.RIGHT: 14
			},
			"hexagons": {
				Edge.HEXAGONS.TOP: 4
			}
		},
		17: {
			"corners": {
				Edge.CORNERS.LEFT: 15,
				Edge.CORNERS.RIGHT: 14
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 4
			}
		},
		18: {
			"corners": {
				Edge.CORNERS.LEFT: 16,
				Edge.CORNERS.RIGHT: 15
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 4
			}
		},
		19: {
			"corners": {
				Edge.CORNERS.LEFT: 17,
				Edge.CORNERS.RIGHT: 16
			},
			"hexagons": {
				Edge.HEXAGONS.BOTTOM: 4
			}
		},
		20: {
			"corners": {
				Edge.CORNERS.LEFT: 17,
				Edge.CORNERS.RIGHT: 9
			},
			"hexagons": {
				Edge.HEXAGONS.TOP: 4
			}
		}
	}
}