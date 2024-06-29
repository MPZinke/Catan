

import { Road } from "./Road.js";
import { Settlement } from "./Settlement.js";


import { ResourceType } from "../../Types.d.js";


export class Tile
{
	coordinate: [number, number];
	roads: [Road?, Road?, Road?, Road?, Road?, Road?];
	settlements: [Settlement?, Settlement?, Settlement?, Settlement?, Settlement?, Settlement?];
	value: number;
	resource_type: string;


	constructor(
		coordinate: [number, number],
		roads: [Road?, Road?, Road?, Road?, Road?, Road?],
		settlements: [Settlement?, Settlement?, Settlement?, Settlement?, Settlement?, Settlement?],
		value: number,
		resource_type: string
	)
	{
		this.coordinate = coordinate;
		this.roads = roads;
		this.settlements = settlements;
		this.value = value;
		this.resource_type = resource_type;
	}
}
