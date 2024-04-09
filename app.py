

from flask import Flask


from database.queries import boards
from game.new import new_game
import gui
import setup


app = Flask("Catan")


@app.route("/new/<int:board_id>")
def new(board_id: int):
	ports, roads, settlements, tiles = new_game(board_id)
	ports_strings = list(map(str, ports))
	roads_strings = list(map(str, roads))
	settlements_strings = list(map(str, settlements))
	tiles_strings = list(map(str, tiles))
	print(
		"\n".join(ports_strings),
		"\n".join(roads_strings),
		"\n".join(settlements_strings),
		"\n".join(tiles_strings)
	)

	ports_strings = list(map(lambda string: string.replace("\n", "<br/>"), ports_strings))
	roads_strings = list(map(lambda string: string.replace("\n", "<br/>"), roads_strings))
	settlements_strings = list(map(lambda string: string.replace("\n", "<br/>"), settlements_strings))
	tiles_strings = list(map(lambda string: string.replace("\n", "<br/>"), tiles_strings))

	ports_strings = list(map(lambda string: string.replace(" ", "&nbsp;"), ports_strings))
	roads_strings = list(map(lambda string: string.replace(" ", "&nbsp;"), roads_strings))
	settlements_strings = list(map(lambda string: string.replace(" ", "&nbsp;"), settlements_strings))
	tiles_strings = list(map(lambda string: string.replace(" ", "&nbsp;"), tiles_strings))

	br_join = "<br/>".join

	parts_string = br_join([br_join(ports_strings), br_join(roads_strings), br_join(settlements_strings), br_join(tiles_strings)])

	gui.draw_tiles(tiles)
	return f"""
		<html style='font-family: Consolas,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New, monospace;'>
			<body>
				{parts_string}
			<body>
		</html>
	""" 


app.run(host="0.0.0.0", port=80)
