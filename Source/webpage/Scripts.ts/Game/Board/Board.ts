


import { Port, Road, Settlement, Tile } from "./index.js";


import { associate_port_settlements, associate_road_settlements, associate_road_tiles, associate_settlement_tiles } from "./associate.js";


type Robber = null;  // TODO: Create a Robber class


export function construct_board(board_data: any): Board
{
	const id = board_data.id;
	const size = board_data.size;

	const ports: Port[] = board_data.ports.map((port: any) => new Port(port.id, port.type));
	const roads: Road[] = board_data.roads.map((road: any) => new Road(road.id, road.type));
	const robber: Robber = null;
	const settlements: Settlement[] = board_data.settlements.map((settlement: any) => new Settlement(settlement.id, settlement.type));
	const tiles: Tile[] = board_data.tiles.map((tile: any) => new Tile(tile.id, tile.coordinate, tile.value, tile.type));

	associate_port_settlements(board_data, ports, settlements);
	associate_road_settlements(board_data, roads, settlements);
	associate_road_tiles(board_data, roads, tiles);
	associate_settlement_tiles(board_data, settlements, tiles);

	const board = new Board(id, size, ports, roads, robber, settlements, tiles);
	return board;
}


export class Board
{
	id: number;
	size: [number, number];
	ports: Port[];
	roads: Road[];
	robber: Robber;
	settlements: Settlement[];
	tiles: Tile[];

	constructor(id: number, size: [number, number], ports: Port[], roads: Road[], robber: Robber,
		settlements: Settlement[], tiles: Tile[]
	)
	{
		this.id = id;
		this.size = size;
		this.ports = ports;
		this.roads = roads;
		this.robber = robber;
		this.settlements = settlements;
		this.tiles = tiles;
	}
}
