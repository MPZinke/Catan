

import Canvas from "./Canvas.js";
import { construct_game, Game } from "./Game/index.js";


const GAME = construct_game();
const CANVAS = new Canvas(GAME.board.size[0], GAME.board.size[1], 75, 30);
CANVAS.draw_tiles(GAME.board.tiles);
CANVAS.draw_settlements(GAME.board.settlements);
