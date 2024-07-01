

import { HexagonGrid, Hexagon } from "./Layout/index.js";
import { get_game_data } from "./Requests.js";
import { RESOURCE_TYPES } from "./Headers.js";


import { Tile } from "./Game/Board/index.js";



export default class Canvas
{
	readonly color_mapping: {[type: string]: string} = {
		"DESERT": "rgb(189, 160, 106)",
		"WHEAT": "rgb(246, 215, 99)",
		"WOOD": "rgb(74, 111, 62)",
		"SHEEP": "rgb(154, 185, 86)",
		"STONE": "rgb(163, 150, 140)",
		"BRICK": "rgb(139, 83, 48)",
	};

	private canvas: HTMLCanvasElement;
	private context: CanvasRenderingContext2D;
	private hexagon_grid: HexagonGrid;
	board_data: any;


	constructor(columns: number, rows: number, hexagon_height: number)
	{
		this.canvas = document.getElementById("canvas")! as HTMLCanvasElement;
		this.context = this.canvas.getContext('2d')!;

		this.hexagon_grid = new HexagonGrid(columns, rows, hexagon_height);

		this.board_data = get_game_data();

		this.set_canvas_width_and_height_for_grid();
		this.add_listeners();
	}


	add_listeners()
	{
		const draw_tile = this.draw_tile.bind(this);
		const mouse_click_position: (event: MouseEvent) => [number, number] = this.mouse_click_position.bind(this);
		const hexagon_grid = this.hexagon_grid;

		// FROM: https://stackoverflow.com/a/24384882
		this.canvas.addEventListener('click',
			function(event)
			{
				var mousePos = mouse_click_position(event);
				for(var row = 0; row < hexagon_grid.rows; row++)
				{
					for(var column = 0; column < hexagon_grid.columns; column++)
					{
						const hexagon = hexagon_grid.hexagon(column, row);
						if(hexagon.point_in_hexagon(...mousePos))
						{
							draw_tile(hexagon, "#F00");
						}
					}
				}
			},
			false
		);
	}


	mouse_click_position(event: MouseEvent): [number, number]
	{
		var rectangle = this.canvas.getBoundingClientRect();
		return [event.clientX - rectangle.left, event.clientY - rectangle.top];
	}


	draw_tile(hexagon: Hexagon, color: string="#f00"): void
	{
		// FROM: https://stackoverflow.com/a/4840009
		// Draw Hexagon interior.
		this.context.fillStyle = color;
		this.context.beginPath();
		this.context.moveTo(hexagon.points[0][0], hexagon.points[0][1]);
		for(var index = 1; index < 6; index++)
		{
			this.context.lineTo(hexagon.points[index][0], hexagon.points[index][1]);
		}
		this.context.closePath();
		this.context.fill();

		// Draw Hexagon exterior.
		this.context.beginPath();
		this.context.moveTo(hexagon.points[0][0], hexagon.points[0][1]);
		for(var index = 1; index < 6; index++)
		{
			this.context.lineTo(hexagon.points[index][0], hexagon.points[index][1]);
			this.context.stroke();
		}
		this.context.lineTo(hexagon.points[0][0], hexagon.points[0][1]);
		this.context.stroke();
	}


	draw_tiles(tiles: Tile[])
	{
		tiles.forEach(
			(tile: Tile) =>
			{
				const hexagon = this.hexagon_grid.hexagon(tile.coordinate[0], tile.coordinate[1]);

				const tile_type = tile.type;
				const color = this.color_mapping[Object.keys(RESOURCE_TYPES).find(key => RESOURCE_TYPES[key] === tile_type) as string];
				this.draw_tile(hexagon, color);
			}
		)
	}


	set_canvas_width_and_height_for_grid(): void
	{
		const hexagon_grid = this.hexagon_grid;
		const hexagon_height = hexagon_grid.hexagon_height;

		const radius: number = 2 * hexagon_height / hexagon_grid.SQUAREROOT_3;

		const height: number = hexagon_height * 2 * hexagon_grid.rows + hexagon_height;
		const width: number = (radius * 2) + (hexagon_grid.columns - 1) * (radius * 1.5);

		this.canvas.width = width;
		this.canvas.height = height;

		this.context.fillStyle = "rgb(66, 149, 208)";
		this.context.fillRect(0, 0, width, height);
	}
}