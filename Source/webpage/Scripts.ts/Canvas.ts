

import { HexagonGrid, Hexagon } from "./Layout/index.js";
import { get_game_data } from "./Requests/index.js";
import { RESOURCE_TYPES } from "./Globals.js";


import { Settlement, Tile } from "./Game/Board/index.js";



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


	constructor(columns: number, rows: number, hexagon_height: number, hexagon_padding: number)
	{
		this.canvas = document.getElementById("canvas")! as HTMLCanvasElement;
		this.context = this.canvas.getContext('2d')!;

		this.hexagon_grid = new HexagonGrid(columns, rows, hexagon_height, hexagon_padding);

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


	draw_circle(center_x: number, center_y: number, radius: number)
	{
		this.context.beginPath();
		this.context.arc(center_x, center_y, radius, 0, 2 * Math.PI, false);
		this.context.fillStyle = 'green';
		this.context.fill();
	}


	draw_hexagon(center_x: number, center_y: number, height: number)
	{
		const radius = height * Hexagon.TWO_OVER_SQUAREROOT_3;
		const radius_cos60: number = radius * Hexagon.COS60;
		const radius_sin60: number = radius * Hexagon.SIN60;
		const points: Array<[number, number]> = [
			[center_x - radius_cos60, center_y - radius_sin60],
			[center_x + radius_cos60, center_y - radius_sin60],
			[center_x + radius,  center_y],
			[center_x + radius_cos60, center_y + radius_sin60],
			[center_x - radius_cos60, center_y + radius_sin60],
			[center_x - radius,  center_y]
		];
		this.draw_polygon(points);
	}


	draw_polygon(points: Array<[number, number]>, fill: string="#CCC", outline: string="#CCC")
	{
		this.context.fillStyle = fill;
		this.context.strokeStyle = outline;
		this.context.beginPath();
		this.context.moveTo(points[0][0], points[0][1]);
		for(var index = 1; index < points.length; index++)
		{
			this.context.lineTo(points[index][0], points[index][1]);
			this.context.stroke();
		}

		this.context.closePath();
		this.context.fill();
		this.context.stroke();
	}


	draw_settlement(settlement: Settlement)
	{
		const tile: Tile = settlement.tiles.find((tile: Tile|null) => tile !== null) as Tile;
		const tile_coordinate: [number, number] = tile.coordinate;
		const settlement_direction: number = tile.settlements.findIndex(
			(temp_settlement: Settlement) => settlement.id === temp_settlement.id
		);

		const height: number = this.hexagon_grid.hexagon_padding * .5;
		const radius = height * Hexagon.TWO_OVER_SQUAREROOT_3;
		const radius_cos60: number = radius * Hexagon.COS60;

		const [x, y] = this.hexagon_grid.hexagon(tile_coordinate[0], tile_coordinate[1]).points[settlement_direction];
		const [x_offset, y_offset] = {
			[Tile.Settlements.TOP_LEFT]:     [-radius_cos60, -height],
			[Tile.Settlements.TOP_RIGHT]:    [ radius_cos60, -height],
			[Tile.Settlements.RIGHT]:        [ radius,       0],
			[Tile.Settlements.BOTTOM_RIGHT]: [ radius_cos60, height],
			[Tile.Settlements.BOTTOM_LEFT]:  [-radius_cos60, height],
			[Tile.Settlements.LEFT]:         [-radius,       0],
		}[settlement_direction];

		this.draw_hexagon(x+x_offset, y+y_offset, height);
		// this.draw_circle(x+x_offset, y+y_offset, height);
	}


	draw_settlements(settlements: Settlement[])
	{
		settlements.forEach(
			(settlement: Settlement) =>
			{
				this.draw_settlement(settlement);
			}
		)
	}


	draw_tile(hexagon: Hexagon, color: string="#f00"): void
	{
		// FROM: https://stackoverflow.com/a/4840009
		// Draw Hexagon interior.
		this.draw_polygon(hexagon.points, color, "#000")
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
		const [width, height] = this.hexagon_grid.dimensions();

		this.canvas.width = width;
		this.canvas.height = height;

		this.context.fillStyle = "rgb(66, 149, 208)";
		this.context.fillRect(0, 0, width, height);
	}
}