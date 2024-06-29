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
