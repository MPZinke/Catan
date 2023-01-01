

from Classes.Board import Board


def main():
	parts = {
		"hexagons": {
			1: {
				"corners": {
					"bottom_left": 0,
					"bottom_right": 1,
					"right": 2,
					"top_right": 3,
					"top_left": 4,
					"left": 5
				},
				"edges": {
					"bottom": 0,
					"bottom_right": 1,
					"top_right": 2,
					"top": 3,
					"top_left": 4,
					"bottom_left": 5
				},
				"type": "DESSERT",
				"value": 6
			}
		},
		"corners": {
			0: {
				"hexagons": {
					"top": 0
				},
				"edges": {}
			},
			1: {
				"hexagons": {
					"top": 0
				},
				"edges": {}
			},
			2: {
				"hexagons": {
					"side": 0
				},
				"edges": {}
			},
			3: {
				"hexagons": {
					"bottom": 0
				},
				"edges": {}
			},
			4: {
				"hexagons": {
					"bottom": 0
				},
				"edges": {}
			},
			5: {
				"hexagons": {
					"side": 0
				},
				"edges": {}
			}
		},
		"edges": [
			0,
			1,
			2,
			3,
			4,
			5
		]
	}

	print(Board(parts))
	print()


if(__name__ == "__main__"):
	main()
