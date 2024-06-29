


import { Port, Road, Settlement, Tile } from "index.js";


type Robber = null;  // TODO: Create a Robber class


export class Board
{
	id: number;
	ports: Port[];
	roads: Road[];
	robber: Robber;
	settlements: Settlement[];
	tiles: Tile[];

	constructor(id: number, ports: Port[], roads: Road[], robber: Robber, settlements: Settlement[], tiles: Tile[])
	{
		this.id = id;
		this.ports = ports;
		this.roads = roads;
		this.robber = robber;
		this.settlements = settlements;
		this.tiles = tiles;
	}
}
