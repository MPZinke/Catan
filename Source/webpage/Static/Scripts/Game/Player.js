export class Player {
    constructor(id, name, development_cards, resources) {
        this.id = id;
        this.name = name;
        this.development_cards = development_cards;
        this.resources = resources;
        this.roads = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null];
        this.settlements = [null, null, null, null, null, null, null, null, null];
    }
}
