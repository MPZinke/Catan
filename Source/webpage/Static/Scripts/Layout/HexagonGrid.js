import { Hexagon } from "./Hexagon.js";
export class HexagonGrid {
    constructor(columns, rows, hexagon_height, hexagon_padding) {
        this.COS60 = 0.5;
        this.SIN60 = 0.8660254037844386;
        this.SQUAREROOT_2_OVER_2 = 0.7071067812;
        this.SQUAREROOT_3 = 1.7320508076;
        this.ONE_OVER_SQUAREROOT_3 = 0.5773502692;
        this.TWO_OVER_SQUAREROOT_3 = 1.1547005384;
        this.columns = columns;
        this.rows = rows;
        this.hexagon_height = hexagon_height;
        this.hexagon_padding = hexagon_padding;
        this.grid = [];
        for (let row = 0; row < rows; row++) {
            this.grid.push([]);
            for (let column = 0; column < columns; column++) {
                const center_x = this.x_position_for_index(column);
                const center_y = this.y_position_for_index(column, row);
                this.grid[row].push(new Hexagon(center_x, center_y, hexagon_height, hexagon_padding));
            }
        }
    }
    x_position_for_index(column) {
        const padding_over_2 = this.hexagon_padding * .5;
        const total_height = padding_over_2 + this.hexagon_height;
        const initial_center = (padding_over_2 + total_height) * this.TWO_OVER_SQUAREROOT_3;
        const incremental_distance = column * this.SQUAREROOT_3 * total_height;
        const distance_to_hexagon_center = initial_center + incremental_distance;
        return distance_to_hexagon_center;
    }
    y_position_for_index(column, row) {
        const padding_over_2 = this.hexagon_padding * .5;
        const offset_for_column_index = (this.hexagon_height + padding_over_2) * (column & 0b1);
        const initial_center = this.hexagon_padding + this.hexagon_height;
        const incremental_distance = (padding_over_2 + this.hexagon_height) * 2 * row;
        const distance_to_hexagon_center = offset_for_column_index + initial_center + incremental_distance;
        return distance_to_hexagon_center;
    }
    dimensions() {
        const padding_over_2 = this.hexagon_padding * .5;
        const width_exterior_padding = this.hexagon_padding * this.TWO_OVER_SQUAREROOT_3;
        const hexagon_width = (padding_over_2 + this.hexagon_height) * this.TWO_OVER_SQUAREROOT_3 * 2;
        const incremental_width = .75 * hexagon_width * (this.columns - 1);
        const width = width_exterior_padding + hexagon_width + incremental_width;
        const height_exterior_padding = this.hexagon_padding;
        const height_offset = +(this.columns > 1) * this.hexagon_height;
        const hexagons_height = this.rows * (this.hexagon_height * 2 + this.hexagon_padding);
        const height = height_exterior_padding + height_offset + hexagons_height;
        return [width, height];
    }
    hexagon(column, row) {
        if (column > this.columns || row > this.rows) {
            throw new Error(`Column-Row index [${column}-${row}] is out of range [${this.columns}-${this.rows}]`);
        }
        return this.grid[row][column];
    }
}
