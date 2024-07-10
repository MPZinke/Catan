

import { Port, Road, Settlement, Tile } from "./index.js";


export function associate_port_settlements(board_data: any, ports: Port[], settlements: Settlement[])
{
	const port_dicts: any[] = board_data.ports as any[];
	const settlement_dicts: any[] = board_data.settlements as any[];
	for(var port_dicts_index = 0; port_dicts_index < port_dicts.length; port_dicts_index++)
	{
		const port_id: number = port_dicts[port_dicts_index].id;
		const port: Port = ports.find(port => port.id == port_id)!;

		for(var port_settlement_index = 0; port_settlement_index < port.settlements.length; port_settlement_index++)
		{
			const settlement_id = port_dicts[port_dicts_index].settlements[port_settlement_index];
			if(settlement_id == null)
			{
				continue;
			}

			const settlement: Settlement = settlements.find(settlement => settlement.id == settlement_id)!;
			port.settlements[port_settlement_index] = settlement;
			const settlement_dict: any = settlement_dicts.find(dict => dict.id == settlement_id)!;
			const settlement_port_index: number = settlement_dict.ports.indexOf(port_id);

			settlement.ports[settlement_port_index] = port;
		}
	}
}


export function associate_road_settlements(board_data: any, roads: Road[], settlements: Settlement[])
{
	const road_dicts: any[] = board_data.roads as any[];
	const settlement_dicts: any[] = board_data.settlements as any[];
	for(var road_dicts_index = 0; road_dicts_index < road_dicts.length; road_dicts_index++)
	{
		const road_id: number = road_dicts[road_dicts_index].id;
		const road: Road = roads.find(road => road.id == road_id)!;

		for(var road_settlement_index = 0; road_settlement_index < road.settlements.length; road_settlement_index++)
		{
			const settlement_id = road_dicts[road_dicts_index].settlements[road_settlement_index];
			if(settlement_id == null)
			{
				continue;
			}

			const settlement: Settlement = settlements.find(settlement => settlement.id == settlement_id)!;
			road.settlements[road_settlement_index] = settlement;
			const settlement_dict: any = settlement_dicts.find(dict => dict.id == settlement_id)!;
			const settlement_road_index: number = settlement_dict.roads.indexOf(road_id);

			settlement.roads[settlement_road_index] = road;
		}
	}
}


export function associate_road_tiles(board_data: any, roads: Road[], tiles: Tile[])
{
	const road_dicts: any[] = board_data.roads as any[];
	const tile_dicts: any[] = board_data.tiles as any[];
	for(var road_dicts_index = 0; road_dicts_index < road_dicts.length; road_dicts_index++)
	{
		const road_id: number = road_dicts[road_dicts_index].id;
		const road: Road = roads.find(road => road.id == road_id)!;

		for(var road_tile_index = 0; road_tile_index < road.tiles.length; road_tile_index++)
		{
			const tile_id = road_dicts[road_dicts_index].tiles[road_tile_index];
			if(tile_id == null)
			{
				continue;
			}

			const tile: Tile = tiles.find(tile => tile.id == tile_id)!;
			road.tiles[road_tile_index] = tile;
			const tile_dict: any = tile_dicts.find(dict => dict.id == tile_id)!;
			const tile_road_index: number = tile_dict.roads.indexOf(road_id);

			tile.roads[tile_road_index] = road;
		}
	}
}


export function associate_settlement_tiles(board_data: any, settlements: Settlement[], tiles: Tile[])
{
	const settlement_dicts: any[] = board_data.settlements as any[];
	const tile_dicts: any[] = board_data.tiles as any[];
	for(var settlement_dicts_index = 0; settlement_dicts_index < settlement_dicts.length; settlement_dicts_index++)
	{
		const settlement_id: number = settlement_dicts[settlement_dicts_index].id;
		const settlement: Settlement = settlements.find(settlement => settlement.id == settlement_id)!;

		for(var settlement_tile_index = 0; settlement_tile_index < settlement.tiles.length; settlement_tile_index++)
		{
			const tile_id = settlement_dicts[settlement_dicts_index].tiles[settlement_tile_index];
			if(tile_id == null)
			{
				continue;
			}

			const tile: Tile = tiles.find(tile => tile.id == tile_id)!;
			settlement.tiles[settlement_tile_index] = tile;
			const tile_dict: any = tile_dicts.find(dict => dict.id == tile_id)!;
			const tile_settlement_index: number = tile_dict.settlements.indexOf(settlement_id);

			tile.settlements[tile_settlement_index] = settlement;
		}
	}
}
