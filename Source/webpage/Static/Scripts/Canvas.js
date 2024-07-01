import { HexagonGrid } from "./Layout/index.js";
import { get_game_data } from "./Requests.js";
import { RESOURCE_TYPES } from "./Headers.js";
export default class Canvas {
    constructor(columns, rows, hexagon_height) {
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
        this.hexagon_grid = new HexagonGrid(columns, rows, hexagon_height);
        this.board_data = get_game_data();
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
    draw_tile(hexagon, color = "#f00") {
        this.context.fillStyle = color;
        this.context.beginPath();
        this.context.moveTo(hexagon.points[0][0], hexagon.points[0][1]);
        for (var index = 1; index < 6; index++) {
            this.context.lineTo(hexagon.points[index][0], hexagon.points[index][1]);
        }
        this.context.closePath();
        this.context.fill();
        this.context.beginPath();
        this.context.moveTo(hexagon.points[0][0], hexagon.points[0][1]);
        for (var index = 1; index < 6; index++) {
            this.context.lineTo(hexagon.points[index][0], hexagon.points[index][1]);
            this.context.stroke();
        }
        this.context.lineTo(hexagon.points[0][0], hexagon.points[0][1]);
        this.context.stroke();
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
        const hexagon_grid = this.hexagon_grid;
        const hexagon_height = hexagon_grid.hexagon_height;
        const radius = 2 * hexagon_height / hexagon_grid.SQUAREROOT_3;
        const height = hexagon_height * 2 * hexagon_grid.rows + hexagon_height;
        const width = (radius * 2) + (hexagon_grid.columns - 1) * (radius * 1.5);
        this.canvas.width = width;
        this.canvas.height = height;
        this.context.fillStyle = "rgb(66, 149, 208)";
        this.context.fillRect(0, 0, width, height);
    }
}
