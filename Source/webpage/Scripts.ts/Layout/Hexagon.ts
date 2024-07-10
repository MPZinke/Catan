

import { Directions } from "../Types.d.js";


import { DIRECTIONS } from "../Globals.js";


export class Hexagon
{
	static readonly COS60: number = 0.5;
	static readonly SIN60: number = 0.8660254037844386;
	static readonly SQUAREROOT_3: number = 1.7320508076;
	static readonly TWO_OVER_SQUAREROOT_3: number = 1.1547005384;

	static readonly Corners: Directions = DIRECTIONS["Side's Corners"];

	x: number;
	y: number;
	height: number;
	padding: number;
	radius: number;
	points: Array<[number, number]>;

	constructor(center_x: number, center_y: number, height: number, padding: number)
	{
		this.x = center_x;
		this.y = center_y;
		this.height = height;
		this.padding = padding;
		this.radius = height * Hexagon.TWO_OVER_SQUAREROOT_3;
		
		const radius_cos60: number = this.radius * Hexagon.COS60;

		this.points = Array(6);
		this.points[Hexagon.Corners.TOP_LEFT    ] = [this.x - radius_cos60, this.y - height];
		this.points[Hexagon.Corners.TOP_RIGHT   ] = [this.x + radius_cos60, this.y - height];
		this.points[Hexagon.Corners.RIGHT       ] = [this.x + this.radius,  this.y];
		this.points[Hexagon.Corners.BOTTOM_RIGHT] = [this.x + radius_cos60, this.y + height];
		this.points[Hexagon.Corners.BOTTOM_LEFT ] = [this.x - radius_cos60, this.y + height];
		this.points[Hexagon.Corners.LEFT        ] = [this.x - this.radius,  this.y];
	}


	point_in_hexagon(x: number, y: number): boolean
	/*
	Points outside of the encompassing square can be trivially rejected.
	 _______________
	|  /         \  |
	| /           \ | 
	|/             \|
	|\             /|
	| \           / |
	|__\_________/__|

	If something is within the square, then the hexagon can be broken up into 3 main parts & 5 subparts.
	
	Main parts: left (L), center (C), right (R).
	    _________
	   /|       |\  
	  / |       | \ 
	 / L|   C   |R \
	 \  |       |  /
	  \ |       | /
	   \|_______|/  

	Subparts: left-top (LT), left-bottom (LB), right-top (RT), and right-bottom (RB).
	    _________     
	   /|       |\  
	LT/ |       | \RT 
	 /__|   C   |__\
	 \  |       |  /
	LB\ |       | /RB
	   \|_______|/  


	For left (L) and right (R), the following formulae can be used based on lines left-top (LT), left-bottom (LB),
	 right-top (RT), and right-bottom (RB):
	|	m = (y2 - y1) / (x2 - x1)
	|	y - y1 = m(x - x1) 
	|	y = m(x - x1) + y1
	*/
	{
		// Trivial rejects
		if(x < this.x - this.radius || this.x + this.radius < x)
		{
			return false;
		}
		if(y < this.y - this.height || this.y + this.height < y)
		{
			return false;
		}


		if(x < this.points[0][0] || this.points[1][0] < x)
		{
			let x1: number;
			let x2: number;
			let y1: number;
			let y2: number;

			if(y <= this.y)  // Top
			{
				y1 = this.y - this.height;
				y2 = this.y;

				if(x < this.points[0][0])  // Top-left
				{
					x1 = this.points[0][0];
					x2 = this.x - this.radius;
				}
				else  // Top-right
				{
					x1 = this.points[1][0];
					x2 = this.x + this.radius;
				}
			}
			else  // Bottom
			{
				y1 = this.y;
				y2 = this.y + this.height;

				if(x < this.points[0][0])  // Bottom-left
				{
					x1 = this.x - this.radius;
					x2 = this.points[4][0];
				}
				else  // Bottom-right
				{
					x1 = this.x + this.radius;
					x2 = this.points[3][0];
				}
			}

			const slope: number = this.height / (x2 - x1);
			const y_value_for_x: number = slope * (x - x1) + y1;
			if(y > this.y)
			{
				return y <= y_value_for_x;
			}
			else
			{
				return y_value_for_x <= y;
			}
		}

		// Should be within center (C) of hexagon otherwise, it would have been rejected by trivial reject.
		return true;
	}
}
