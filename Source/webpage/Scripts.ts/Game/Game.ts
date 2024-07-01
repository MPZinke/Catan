

import { Player } from "Player.js";
import { construct_board, Board } from "./Board/index.js";


import { get_game_data } from "../Requests.js";


import { ResourceType } from "../Types.d.js";


export function construct_game(): Game
{
	const game_data: any = get_game_data();

	const id: number = game_data.id;
	const board: Board = construct_board(game_data.board);

	const game = new Game(id, board, [], []);
	return game;
}


export class Game
{
	id: number;
	board: Board;
	players: Player[];
	resources: ResourceType[];


	constructor(id: number, board: Board, players: Player[], resources: ResourceType[])
	{
		this.id = id;
		this.board = board;
		this.players = players;
		this.resources = resources;
	}
}
