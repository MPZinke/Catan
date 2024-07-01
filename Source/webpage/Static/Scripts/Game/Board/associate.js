export function associate_port_settlements(board_data, ports, settlements) {
    const port_dicts = board_data.ports;
    const settlement_dicts = board_data.settlements;
    for (var port_dicts_index = 0; port_dicts_index < port_dicts.length; port_dicts_index++) {
        const port_id = port_dicts[port_dicts_index].id;
        const port = ports.find(port => port.id == port_id);
        for (var port_settlement_index = 0; port_settlement_index < port.settlements.length; port_settlement_index++) {
            const settlement_id = port_dicts[port_dicts_index].settlements[port_settlement_index];
            if (settlement_id == null) {
                continue;
            }
            const settlement = settlements.find(settlement => settlement.id == settlement_id);
            port.settlements[settlement_id] = settlement;
            const settlement_dict = settlement_dicts.find(dict => dict.id == settlement_id);
            const settlement_port_index = settlement_dict.ports.indexOf(port_id);
            settlement.ports[settlement_port_index] = port;
        }
    }
}
export function associate_road_settlements(board_data, roads, settlements) {
    const road_dicts = board_data.roads;
    const settlement_dicts = board_data.settlements;
    for (var road_dicts_index = 0; road_dicts_index < road_dicts.length; road_dicts_index++) {
        const road_id = road_dicts[road_dicts_index].id;
        const road = roads.find(road => road.id == road_id);
        for (var road_settlement_index = 0; road_settlement_index < road.settlements.length; road_settlement_index++) {
            const settlement_id = road_dicts[road_dicts_index].settlements[road_settlement_index];
            if (settlement_id == null) {
                continue;
            }
            const settlement = settlements.find(settlement => settlement.id == settlement_id);
            road.settlements[settlement_id] = settlement;
            const settlement_dict = settlement_dicts.find(dict => dict.id == settlement_id);
            const settlement_road_index = settlement_dict.roads.indexOf(road_id);
            settlement.roads[settlement_road_index] = road;
        }
    }
}
export function associate_road_tiles(board_data, roads, tiles) {
    const road_dicts = board_data.roads;
    const tile_dicts = board_data.tiles;
    for (var road_dicts_index = 0; road_dicts_index < road_dicts.length; road_dicts_index++) {
        const road_id = road_dicts[road_dicts_index].id;
        const road = roads.find(road => road.id == road_id);
        for (var road_tile_index = 0; road_tile_index < road.tiles.length; road_tile_index++) {
            const tile_id = road_dicts[road_dicts_index].tiles[road_tile_index];
            if (tile_id == null) {
                continue;
            }
            const tile = tiles.find(tile => tile.id == tile_id);
            road.tiles[tile_id] = tile;
            const tile_dict = tile_dicts.find(dict => dict.id == tile_id);
            const tile_road_index = tile_dict.roads.indexOf(road_id);
            tile.roads[tile_road_index] = road;
        }
    }
}
export function associate_settlement_tiles(board_data, settlements, tiles) {
    const settlement_dicts = board_data.settlements;
    const tile_dicts = board_data.tiles;
    for (var settlement_dicts_index = 0; settlement_dicts_index < settlement_dicts.length; settlement_dicts_index++) {
        const settlement_id = settlement_dicts[settlement_dicts_index].id;
        const settlement = settlements.find(settlement => settlement.id == settlement_id);
        for (var settlement_tile_index = 0; settlement_tile_index < settlement.tiles.length; settlement_tile_index++) {
            const tile_id = settlement_dicts[settlement_dicts_index].tiles[settlement_tile_index];
            if (tile_id == null) {
                continue;
            }
            const tile = tiles.find(tile => tile.id == tile_id);
            settlement.tiles[tile_id] = tile;
            const tile_dict = tile_dicts.find(dict => dict.id == tile_id);
            const tile_settlement_index = tile_dict.settlements.indexOf(settlement_id);
            tile.settlements[tile_settlement_index] = settlement;
        }
    }
}
