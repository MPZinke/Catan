

import { Directions, ResourceType } from "../../Types.d.js";


import { Road, Settlement } from "./index.js";


import { DIRECTIONS } from "../../Globals.js";


export class Tile
{
	static readonly Settlements: Directions = DIRECTIONS["Side's Corners"];
	static readonly Roads: Directions = DIRECTIONS["Side's Edges"];

	id: number;
	coordinate: [number, number];
	value: number;
	type: number;
	roads: [Road|null, Road|null, Road|null, Road|null, Road|null, Road|null];
	settlements: [Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null];


	constructor(id: number, coordinate: [number, number], value: number, type: number)
	{
		this.id = id;
		this.coordinate = coordinate;
		this.value = value;
		this.type = type;

		this.roads = [null, null, null, null, null, null];
		this.settlements = [null, null, null, null, null, null];
	}
}
