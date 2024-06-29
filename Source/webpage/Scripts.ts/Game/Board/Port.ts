

import { Settlement } from "./index.js";


import { ResourceType } from "../../Types.d.js";


export class Port
{
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
