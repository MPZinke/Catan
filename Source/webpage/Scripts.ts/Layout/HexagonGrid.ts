

import { Hexagon } from "./Hexagon.js";


export class HexagonGrid
/*
Creates a grid of hexagons at a specified size within a give area.
---
When measuring from the center of a hexagon to a vertice as depicted in Figure 1, the following formula can be
 applied:
	w = 2s, h = (√3)s
Figure 1.
  |<---- 2s ----->|  
      _________      _
     /         \     ↑
    /           \    |
   /      ___S___\  (√3)s
   \             /   |
    \           /    |
     \_________/     ↓
                     ‾
	
Therefore, we determine the ratio of 
	w : h => 2s : (√3)s

Applying this for measuring from the center of a hexagon to a side as depicted in Figure 2, the following is
 derived:
	    y = .5 h     ==     2y = h
	=>  y = .5 (√3)s
	=> 2y = (√3)s
	=> 2y/√3 = s
Using w = 2s,
	   w = 2(2y/√3)
	=> w = 4y/√3

Figure 2.
  |<--- 4y/√3 --->|   
      _________      _
     /    |    \     ↑
    /     y     \    |
   /      |      \  2y
   \             /   |
    \           /    |
     \_________/     ↓
                     ‾

Additional important distances between hexagon centers in the grid shown below are as follow:
	   horizontal distance = (3/4)w
	   vertical distance   = (1/2)h
	=> horizontal distance = (3/4)(4y/√3)
	   vertical distance   = (1/2)(2y)
	=> horizontal distance = (3y/√3) => (√3)y
	   vertical distance   = y

Figure 3.
      _________
     /         \
    /           \
   /      .      \_____     _
   \             /          ↑
    \           /           y
     \_________/       .    ↓
               \            ‾
                \       
          |<-- (√3)y ->|


Finally, first hexagon will start in the top left settlement with its top side against the top of the area and the left
 settlement against the left side. Numbering starts at [0, 0]. The first hexagon of the odd rows will be shifted down
 by `y` units and to the right by `(√3)y` units.

Links:
- https://www.redblobgames.com/grids/hexagons/
*/
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
	/*
	Determines a hexagon's center x_position give an index.
	---
	Given radius `r` and height `h`
		r = 2 * h / √3

	            2y/√3
	          |<----->|  
	      _________      _
	     /    |    \     ↑
	    /     y     \    y
	   /      |      \   ↓
	   \             /    
	    \           /     
	     \_________/      
	and distance between columns `d`

		d = 3 / 4 * 2 * r
	      _________
	     /         \
	    /           \
	   /      .      \_____ 
	   \             /      
	    \           /       
	     \_________/       .
	               \        
	                \       
	          |<-- 1.5r ->|
	then
		d = 3 / 4 * 2 * 2 * h / √3
	 => d = 12 * h / 4 / √3
	 => d = 6 * h / 2 / √3
	 => d = 6 * √3 * h / 2 / 3
	 => d = 6 * √3 * h / 6
	 => d = √3 * h
	*/
	{
		const padding_over_2 = this.hexagon_padding * .5;
		const total_height = padding_over_2 + this.hexagon_height;
		const total_radius = total_height * this.TWO_OVER_SQUAREROOT_3;
		const initial_hexagon_center = total_radius;
		const additional_radius = column * this.SQUAREROOT_3 * total_height;
		const distance_to_hexagon_center = initial_hexagon_center + additional_radius;

		return distance_to_hexagon_center;
	}


	y_position_for_index(column: number, row: number): number
	{
		// The span to the current hexagon's top.
		// Height offset + padding offset.
		const offset_for_column_index: number = (this.hexagon_height + this.hexagon_padding * .5) * (column & 0b1);
		const padding_distance: number = this.hexagon_padding + row * this.hexagon_padding;
		const hexagon_distance: number = this.hexagon_height * 2 * row;
		const distance_to_hexagon_top: number = offset_for_column_index + padding_distance + hexagon_distance;
		// Adds height to get to center.
		const distance_to_hexagon_center: number = distance_to_hexagon_top + this.hexagon_height;

		return distance_to_hexagon_center;
	}


	dimensions(): [number, number]
	{
		// Width
		const hexagon_padding_sin60 = this.hexagon_padding * this.SIN60;
		const width_padding: number = hexagon_padding_sin60 * this.columns + hexagon_padding_sin60;
		const hexagon_width: number = this.hexagon_height * this.TWO_OVER_SQUAREROOT_3 * 2;  // radius * 2
		const width_distance: number = hexagon_width + .75 * hexagon_width * (this.columns - 1);
		const width: number = width_padding + width_distance;

		// Height
		const height_padding_distance: number = this.hexagon_padding + this.rows * this.hexagon_padding;
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
