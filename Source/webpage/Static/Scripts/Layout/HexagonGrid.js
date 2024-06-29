import { Hexagon } from "./Hexagon.js";
export class HexagonGrid {
    constructor(columns, rows, hexagon_height) {
        this.COS60 = 0.5;
        this.SIN60 = 0.8660254037844386;
        this.SQUAREROOT_3 = 1.7320508076;
        this.columns = columns;
        this.rows = rows;
        this.hexagon_height = hexagon_height;
        this.grid = [];
        for (let row = 0; row < rows; row++) {
            this.grid.push([]);
            for (let column = 0; column < columns; column++) {
                const center_x = this.x_position_for_index(column);
                const center_y = this.y_position_for_index(column, row);
                this.grid[row].push(new Hexagon(center_x, center_y, hexagon_height));
            }
        }
    }
    x_position_for_index(column) {
        const incremental_increase = 2 + (3 * column);
        const size_multiplier = this.hexagon_height * incremental_increase / this.SQUAREROOT_3;
        const distance_to_hexagon_center = Math.floor(size_multiplier);
        return distance_to_hexagon_center;
    }
    y_position_for_index(column, row) {
        const offset_for_column_index = this.hexagon_height * (column & 0b1);
        const distance_to_hexagon_top = this.hexagon_height * 2 * row + offset_for_column_index;
        const distance_to_hexagon_center = distance_to_hexagon_top + this.hexagon_height;
        return distance_to_hexagon_center;
    }
    hexagon(column, row) {
        if (column > this.columns || row > this.rows) {
            throw new Error(`Column-Row index [${column}-${row}] is out of range [${this.columns}-${this.rows}]`);
        }
        return this.grid[row][column];
    }
}
