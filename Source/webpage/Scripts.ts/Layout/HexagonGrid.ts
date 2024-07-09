

import { Hexagon } from "./Hexagon.js";


export class HexagonGrid
{
	readonly COS60: number = 0.5;
	readonly SIN60: number = 0.8660254037844386;
	readonly SQUAREROOT_2_OVER_2: number = 0.7071067812;
	readonly SQUAREROOT_3: number = 1.7320508076;
	readonly TWO_OVER_SQUAREROOT_3: number = 1.1547005384;

	columns: number;
	rows: number;
	hexagon_height: number;
	hexagon_padding: number;
	grid: Hexagon[][];


	constructor(columns: number, rows: number, hexagon_height: number, hexagon_padding: number)
	{
		this.columns = columns;
		this.rows = rows;
		this.hexagon_height = hexagon_height;
		this.hexagon_padding = hexagon_padding;

		this.grid = [];
		for(let row = 0; row < rows; row++)
		{
			this.grid.push([]);
			for(let column = 0; column < columns; column++)
			{
				const center_x: number = this.x_position_for_index(column);
				const center_y: number = this.y_position_for_index(column, row);
				this.grid[row].push(new Hexagon(center_x, center_y, hexagon_height, hexagon_padding));
			}
		}
	}


	x_position_for_index(column: number): number
	{
		const incremental_increase: number = 2 + (3 * column);
		const size_multiplier: number = this.hexagon_height * incremental_increase / this.SQUAREROOT_3;
		const padding_distance: number = (column + 1) * this.hexagon_padding;
		const distance_to_hexagon_center: number = Math.floor(size_multiplier + padding_distance);
		return distance_to_hexagon_center;
	}


	y_position_for_index(column: number, row: number): number
	{
		// The span to the current hexagon's top.
		const offset_for_column_index: number = (this.hexagon_height + this.hexagon_padding * .5) * (column & 0b1);
		const padding_distance: number = this.hexagon_padding * (row + 1);
		const hexagon_distance: number = this.hexagon_height * 2 * row;
		const distance_to_hexagon_top: number = padding_distance + hexagon_distance + offset_for_column_index;
		// Adds height to get to center.
		const distance_to_hexagon_center: number = distance_to_hexagon_top + this.hexagon_height;
		return distance_to_hexagon_center;
	}


	dimensions(): [number, number]
	{
		// Width
		const width_padding: number = this.hexagon_padding * this.columns + this.hexagon_padding;
		const hexagon_width: number = this.hexagon_height * this.TWO_OVER_SQUAREROOT_3 * 2;  // radius * 2
		const width_distance: number = hexagon_width + .75 * hexagon_width * (this.columns - 1);
		const width: number = width_padding + width_distance;

		// Height
		const height_padding_distance: number = this.hexagon_padding * (this.rows + 1);
		const height_hexagon_distance: number = this.rows * this.hexagon_height * 2;
		const height_offset: number = +(this.columns > 1) * this.hexagon_height;
		const height: number = height_padding_distance + height_hexagon_distance + height_offset;

		return [width, height];
	}


	hexagon(column: number, row: number): Hexagon
	{
		if(column > this.columns || row > this.rows)
		{
			throw new Error(`Column-Row index [${column}-${row}] is out of range [${this.columns}-${this.rows}]`);
		}

		return this.grid[row][column];
	}
}
