

import { Directions, ResourceType, SettlementType } from "../../Types.d.js";


import { Port, Road, Tile } from "./index.js";
import { Player } from "../Player.js";


import { DIRECTIONS } from "../../Globals.js";


export class Settlement
{
	static readonly Port: Directions = DIRECTIONS["Corner's Sides"];
	static readonly Roads: Directions = DIRECTIONS["Corner's Edges"];
	static readonly Tiles: Directions = DIRECTIONS["Corner's Sides"];

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
