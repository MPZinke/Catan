import { DIRECTIONS } from "../../Globals.js";
export class Settlement {
    constructor(id, type) {
        this.id = id;
        this.type = type;
        this.ports = [null, null, null];
        this.roads = [null, null, null];
        this.tiles = [null, null, null];
        this.player = null;
    }
}
Settlement.Port = DIRECTIONS["Corner's Sides"];
Settlement.Roads = DIRECTIONS["Corner's Edges"];
Settlement.Tiles = DIRECTIONS["Corner's Sides"];
