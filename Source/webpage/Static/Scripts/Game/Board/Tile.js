export class Tile {
    constructor(coordinate, roads, settlements, value, resource_type) {
        this.coordinate = coordinate;
        this.roads = roads;
        this.settlements = settlements;
        this.value = value;
        this.resource_type = resource_type;
    }
}
