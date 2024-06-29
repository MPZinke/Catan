

import { Road, Settlement } from "./Board/index.js";


import { ResourceCount, ResourceType } from "../Types.d.js";


export class Player
{
	id: number;
	name: string;
	development_cards: ResourceCount[];  // TODO: add correct type
	resources: ResourceCount[];

	roads: [Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null, Road|null];
	settlements: [Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null, Settlement|null];


	constructor(id: number, name: string, development_cards: ResourceCount[], resources: ResourceCount[])
	{
		this.id = id;
		this.name = name;
		this.development_cards = development_cards;
		this.resources = resources;
		this.roads = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null];
		this.settlements = [null, null, null, null, null, null, null, null, null];
	}
}
