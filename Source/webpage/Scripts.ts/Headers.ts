

import { get_resource_types } from "./Requests.js";
import { HexagonGrid } from "./Layout/index.js";
import Canvas from "./Canvas.js";
import { construct_game, Game } from "./Game/index.js";


export const RESOURCE_TYPES = get_resource_types();


const GAME = construct_game();
const CANVAS = new Canvas(GAME.board.size[0], GAME.board.size[1], 75, 20);
CANVAS.draw_tiles(GAME.board.tiles);
