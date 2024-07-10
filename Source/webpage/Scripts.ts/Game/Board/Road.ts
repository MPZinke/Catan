

import { Directions, ResourceType } from "../../Types.d.js";


import { Settlement, Tile } from "./index.js";
import { Player } from "../Player.js";


import { DIRECTIONS } from "../../Globals.js";


export class Road
{
	static readonly Settlements: Directions = DIRECTIONS["Edge's Corners"];
	static readonly Tiles: Directions = DIRECTIONS["Edge's Sides"];

	id: number;
	type: ResourceType;

	settlements: [Settlement|null, Settlement|null];
	tiles: [Tile|null, Tile|null];
	player: Player|null;


	constructor(id: number, type: ResourceType)
	{
		this.id = id;
		this.type = type;

		this.settlements = [null, null];
		this.tiles = [null, null];

		this.player = null;
	}
}
