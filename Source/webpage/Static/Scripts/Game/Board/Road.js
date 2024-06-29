export class Road {
    constructor(id, type) {
        this.id = id;
        this.type = type;
        this.settlements = [null, null];
        this.tiles = [null, null];
        this.player = null;
    }
}
