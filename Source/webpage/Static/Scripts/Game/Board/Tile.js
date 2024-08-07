import { DIRECTIONS } from "../../Globals.js";
export class Tile {
    constructor(id, coordinate, value, type) {
        this.id = id;
        this.coordinate = coordinate;
        this.value = value;
        this.type = type;
        this.roads = [null, null, null, null, null, null];
        this.settlements = [null, null, null, null, null, null];
    }
}
Tile.Settlements = DIRECTIONS["Side's Corners"];
Tile.Roads = DIRECTIONS["Side's Edges"];
