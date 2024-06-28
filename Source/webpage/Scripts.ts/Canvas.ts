

import HexagonGrid from "./HexagonGrid.js";
import Hexagon from "./Hexagon.js";


export default class Canvas
{
	private canvas: HTMLCanvasElement;
	private context: CanvasRenderingContext2D;
	private hexagon_grid: HexagonGrid;

	constructor(hexagon_grid: HexagonGrid)
	{
		this.canvas = document.getElementById("canvas")! as HTMLCanvasElement;
		this.context = this.canvas.getContext('2d')!;

		this.hexagon_grid = hexagon_grid;
		for(var row = 0; row < hexagon_grid.rows; row++)
		{
			for(var column = 0; column < hexagon_grid.columns; column++)
			{
				this.draw_tile(hexagon_grid.hexagon(column, row));
			}		
		}

		this.set_canvas_width_and_height_for_grid();
		this.add_listeners();
		this.draw_tiles();
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
							draw_tile(hexagon, "00F");
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


	draw_tiles()
	{
		for(var row = 0; row < this.hexagon_grid.rows; row++)
		{
			for(var column = 0; column < this.hexagon_grid.columns; column++)
			{
				const hexagon = this.hexagon_grid.hexagon(column, row);
				this.draw_tile(hexagon);
			}
		}
	}


	set_canvas_width_and_height_for_grid(): void
	{
		const hexagon_grid = this.hexagon_grid;

		const radius: number = 2 * hexagon_grid.hexagon_height / hexagon_grid.SQUAREROOT_3;

		const width_incremental_increase: number = 2 + (3 * hexagon_grid.columns);
		const width_size_multiplier: number = hexagon_grid.hexagon_height * width_incremental_increase / hexagon_grid.SQUAREROOT_3;
		const width: number = Math.floor(width_size_multiplier + radius);
		const height: number = hexagon_grid.hexagon_height * 2 * hexagon_grid.rows + hexagon_grid.hexagon_height;

		console.log(width);
		console.log(height);

		this.canvas.width = width;
		this.canvas.height = height;
	}
}