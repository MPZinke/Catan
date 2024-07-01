import { construct_board } from "./Board/index.js";
import { get_game_data } from "../Requests.js";
export function construct_game() {
    const game_data = get_game_data();
    const id = game_data.id;
    const board = construct_board(game_data.board);
    const game = new Game(id, board, [], []);
    return game;
}
export class Game {
    constructor(id, board, players, resources) {
        this.id = id;
        this.board = board;
        this.players = players;
        this.resources = resources;
    }
}
