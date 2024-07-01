

import { Road } from "./Road.js";
import { Settlement } from "./Settlement.js";


import { ResourceType } from "../../Types.d.js";


export class Tile
{
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
