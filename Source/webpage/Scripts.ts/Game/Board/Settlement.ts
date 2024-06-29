

import { Port } from "./Port.js";
import { Road } from "./Road.js";
import { Tile } from "index.js";

import { Player } from "../Player.js";


import { ResourceType, SettlementType } from "../../Types.d.js";


export class Settlement
{
	id: number;
	type: SettlementType;

	ports: [Port|null, Port|null, Port|null];
	roads: [Road|null, Road|null, Road|null];
	tiles: [Tile|null, Tile|null, Tile|null];

	player: Player|null;


	constructor(id: number, type: SettlementType)
	{
		this.id = id;
		this.type = type;

		this.ports = [null, null, null];
		this.roads = [null, null, null];
		this.tiles = [null, null, null];
		this.player = null;
	}
}
