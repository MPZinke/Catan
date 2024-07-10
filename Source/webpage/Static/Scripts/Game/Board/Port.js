import { DIRECTIONS } from "../../Globals.js";
export class Port {
    constructor(id, type) {
        this.id = id;
        this.type = type;
        this.settlements = [null, null, null, null, null, null];
    }
}
Port.Settlements = DIRECTIONS["Side's Corners"];
