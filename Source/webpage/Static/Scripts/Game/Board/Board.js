import { Port, Road, Settlement, Tile } from "./index.js";
import { associate_port_settlements, associate_road_settlements, associate_road_tiles, associate_settlement_tiles } from "./associate.js";
export function construct_board(board_data) {
    const id = board_data.id;
    const size = board_data.size;
    const ports = board_data.ports.map((port) => new Port(port.id, port.type));
    const roads = board_data.roads.map((road) => new Road(road.id, road.type));
    const robber = null;
    const settlements = board_data.settlements.map((settlement) => new Settlement(settlement.id, settlement.type));
    const tiles = board_data.tiles.map((tile) => new Tile(tile.id, tile.coordinate, tile.value, tile.type));
    associate_port_settlements(board_data, ports, settlements);
    associate_road_settlements(board_data, roads, settlements);
    associate_road_tiles(board_data, roads, tiles);
    associate_settlement_tiles(board_data, settlements, tiles);
    const board = new Board(id, size, ports, roads, robber, settlements, tiles);
    return board;
}
export class Board {
    constructor(id, size, ports, roads, robber, settlements, tiles) {
        this.id = id;
        this.size = size;
        this.ports = ports;
        this.roads = roads;
        this.robber = robber;
        this.settlements = settlements;
        this.tiles = tiles;
    }
}
