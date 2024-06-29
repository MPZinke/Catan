

import { Settlement } from "./Settlement.js";
import { Tile } from "./Tile.js";

import { Player } from "../Player.js";

import { ResourceType } from "../../Types.d.js";


export class Road
{
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
