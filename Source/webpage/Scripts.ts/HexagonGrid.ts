

import Hexagon from "./Hexagon.js";


export default class HexagonGrid
{
	readonly COS60: number = 0.5;
	readonly SIN60: number = 0.8660254037844386;
	readonly SQUAREROOT_3: number = 1.7320508076;

	columns: number;
	rows: number;
	hexagon_height: number;
	grid: Hexagon[][];


	constructor(columns: number, rows: number, hexagon_height: number)
	{
		this.columns = columns;
		this.rows = rows;
		this.hexagon_height = hexagon_height;

		this.grid = [];
		for(let row = 0; row < rows; row++)
		{
			this.grid.push([]);
			for(let column = 0; column < columns; column++)
			{
				const center_x: number = this.x_position_for_index(column);
				const center_y: number = this.y_position_for_index(column, row);
				this.grid[row].push(new Hexagon(center_x, center_y, hexagon_height));
			}
		}
	}


	x_position_for_index(column: number): number
	{
		const incremental_increase: number = 2 + (3 * column);
		const size_multiplier: number = this.hexagon_height * incremental_increase / this.SQUAREROOT_3;
		const distance_to_hexagon_center: number = Math.floor(size_multiplier);
		return distance_to_hexagon_center;
	}


	y_position_for_index(column: number, row: number): number
	{
		// The span to the current hexagon's top.
		const offset_for_column_index: number = this.hexagon_height * (column & 0b1);
		const distance_to_hexagon_top: number = this.hexagon_height * 2 * row + offset_for_column_index;
		// Adds height to get to center.
		const distance_to_hexagon_center: number = distance_to_hexagon_top + this.hexagon_height;
		return distance_to_hexagon_center;
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
