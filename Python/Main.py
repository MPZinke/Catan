

from Classes.Board import Board

def main():
	parts = {
		"hexagons": {
			1: {
				"type": "DESSERT",
				"corners": {
					"bottom_left": 1,
					"bottom_right": 2,
					"right": 3,
					"top_right": 4,
					"top_left": 5,
					"left": 6
				},
				"edges": {
					"bottom": 1,
					"bottom_right": 2,
					"top_right": 3,
					"top": 4,
					"top_left": 5,
					"bottom_left": 6
				}
			}
		},
		"points": {
			
		}
	}
	
	print(Board(parts))
	print()
	
	
if(__name__ == "__main__"):
	main()

