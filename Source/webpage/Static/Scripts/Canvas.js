import { HexagonGrid, Hexagon } from "./Layout/index.js";
import { RESOURCE_TYPES } from "./Globals.js";
import { Tile } from "./Game/Board/index.js";
export default class Canvas {
    constructor(columns, rows, hexagon_height, hexagon_padding) {
        this.color_mapping = {
            "DESERT": "rgb(189, 160, 106)",
            "WHEAT": "rgb(246, 215, 99)",
            "WOOD": "rgb(74, 111, 62)",
            "SHEEP": "rgb(154, 185, 86)",
            "STONE": "rgb(163, 150, 140)",
            "BRICK": "rgb(139, 83, 48)",
        };
        this.canvas = document.getElementById("canvas");
        this.context = this.canvas.getContext('2d');
        this.hexagon_grid = new HexagonGrid(columns, rows, hexagon_height, hexagon_padding);
        this.set_canvas_width_and_height_for_grid();
        this.add_listeners();
    }
    add_listeners() {
        const draw_tile = this.draw_tile.bind(this);
        const mouse_click_position = this.mouse_click_position.bind(this);
        const hexagon_grid = this.hexagon_grid;
        this.canvas.addEventListener('click', function (event) {
            var mousePos = mouse_click_position(event);
            for (var row = 0; row < hexagon_grid.rows; row++) {
                for (var column = 0; column < hexagon_grid.columns; column++) {
                    const hexagon = hexagon_grid.hexagon(column, row);
                    if (hexagon.point_in_hexagon(...mousePos)) {
                        draw_tile(hexagon, "#F00");
                    }
                }
            }
        }, false);
    }
    mouse_click_position(event) {
        var rectangle = this.canvas.getBoundingClientRect();
        return [event.clientX - rectangle.left, event.clientY - rectangle.top];
    }
    draw_hexagon(center_x, center_y, height) {
        const radius = height * Hexagon.TWO_OVER_SQUAREROOT_3;
        const radius_cos60 = radius * Hexagon.COS60;
        const radius_sin60 = radius * Hexagon.SIN60;
        const points = [
            [center_x - radius_cos60, center_y - radius_sin60],
            [center_x + radius_cos60, center_y - radius_sin60],
            [center_x + radius, center_y],
            [center_x + radius_cos60, center_y + radius_sin60],
            [center_x - radius_cos60, center_y + radius_sin60],
            [center_x - radius, center_y]
        ];
        this.draw_polygon(points);
    }
    draw_polygon(points, fill = "#CCC", outline = "#CCC") {
        this.context.fillStyle = fill;
        this.context.strokeStyle = outline;
        this.context.beginPath();
        this.context.moveTo(points[0][0], points[0][1]);
        for (var index = 1; index < points.length; index++) {
            this.context.lineTo(points[index][0], points[index][1]);
            this.context.stroke();
        }
        this.context.closePath();
        this.context.fill();
        this.context.stroke();
    }
    draw_settlement(settlement) {
        const tile = settlement.tiles.find((tile) => tile !== null);
        const tile_coordinate = tile.coordinate;
        const settlement_direction = tile.settlements.findIndex((temp_settlement) => settlement.id === temp_settlement.id);
        const height = this.hexagon_grid.hexagon_padding * .5;
        const radius = height * Hexagon.TWO_OVER_SQUAREROOT_3;
        const radius_cos60 = radius * Hexagon.COS60;
        const [x, y] = this.hexagon_grid.hexagon(tile_coordinate[0], tile_coordinate[1]).points[settlement_direction];
        const [x_offset, y_offset] = {
            [Tile.Settlements.TOP_LEFT]: [-radius_cos60, -height],
            [Tile.Settlements.TOP_RIGHT]: [radius_cos60, -height],
            [Tile.Settlements.RIGHT]: [radius, 0],
            [Tile.Settlements.BOTTOM_RIGHT]: [radius_cos60, height],
            [Tile.Settlements.BOTTOM_LEFT]: [-radius_cos60, height],
            [Tile.Settlements.LEFT]: [-radius, 0],
        }[settlement_direction];
        this.draw_hexagon(x + x_offset, y + y_offset, height);
    }
    draw_settlements(settlements) {
        settlements.forEach((settlement) => {
            this.draw_settlement(settlement);
        });
    }
    draw_tile(hexagon, color = "#f00") {
        this.draw_polygon(hexagon.points, color, "#000");
    }
    draw_tiles(tiles) {
        tiles.forEach((tile) => {
            const hexagon = this.hexagon_grid.hexagon(tile.coordinate[0], tile.coordinate[1]);
            const tile_type = tile.type;
            const color = this.color_mapping[Object.keys(RESOURCE_TYPES).find(key => RESOURCE_TYPES[key] === tile_type)];
            this.draw_tile(hexagon, color);
        });
    }
    set_canvas_width_and_height_for_grid() {
        const [width, height] = this.hexagon_grid.dimensions();
        this.canvas.width = width;
        this.canvas.height = height;
        this.context.fillStyle = "rgb(66, 149, 208)";
        this.context.fillRect(0, 0, width, height);
    }
}
