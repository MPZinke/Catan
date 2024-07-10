

import { Directions, ResourceType } from "../../Types.d.js";


import { Settlement } from "./index.js";


import { DIRECTIONS } from "../../Globals.js";


export class Port
{
	static readonly Settlements: Directions = DIRECTIONS["Side's Corners"];

	id: number;
	type: ResourceType;
	settlements: [Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null];


	constructor(id: number, type: ResourceType)
	{
		this.id = id;
		this.type = type;

		this.settlements = [null, null, null, null, null, null];
	}
}
