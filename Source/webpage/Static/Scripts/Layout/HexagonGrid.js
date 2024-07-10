import { Hexagon } from "./Hexagon.js";
export class HexagonGrid {
    constructor(columns, rows, hexagon_height, hexagon_padding) {
        this.COS60 = 0.5;
        this.SIN60 = 0.8660254037844386;
        this.SQUAREROOT_2_OVER_2 = 0.7071067812;
        this.SQUAREROOT_3 = 1.7320508076;
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
        const total_radius = total_height * this.TWO_OVER_SQUAREROOT_3;
        const initial_hexagon_center = total_radius;
        const additional_radius = column * this.SQUAREROOT_3 * total_height;
        const distance_to_hexagon_center = initial_hexagon_center + additional_radius;
        return distance_to_hexagon_center;
    }
    y_position_for_index(column, row) {
        const offset_for_column_index = (this.hexagon_height + this.hexagon_padding * .5) * (column & 0b1);
        const padding_distance = this.hexagon_padding + row * this.hexagon_padding;
        const hexagon_distance = this.hexagon_height * 2 * row;
        const distance_to_hexagon_top = offset_for_column_index + padding_distance + hexagon_distance;
        const distance_to_hexagon_center = distance_to_hexagon_top + this.hexagon_height;
        return distance_to_hexagon_center;
    }
    dimensions() {
        const hexagon_padding_sin60 = this.hexagon_padding * this.SIN60;
        const width_padding = hexagon_padding_sin60 * this.columns + hexagon_padding_sin60;
        const hexagon_width = this.hexagon_height * this.TWO_OVER_SQUAREROOT_3 * 2;
        const width_distance = hexagon_width + .75 * hexagon_width * (this.columns - 1);
        const width = width_padding + width_distance;
        const height_padding_distance = this.hexagon_padding + this.rows * this.hexagon_padding;
        const height_hexagon_distance = this.rows * this.hexagon_height * 2;
        const height_offset = +(this.columns > 1) * this.hexagon_height;
        const height = height_padding_distance + height_hexagon_distance + height_offset;
        return [width, height];
    }
    hexagon(column, row) {
        if (column > this.columns || row > this.rows) {
            throw new Error(`Column-Row index [${column}-${row}] is out of range [${this.columns}-${this.rows}]`);
        }
        return this.grid[row][column];
    }
}
