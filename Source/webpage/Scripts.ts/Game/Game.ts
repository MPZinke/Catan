

import { Player } from "Player.js";
import { Board } from "Board/index.js";


import { ResourceType } from "../Types.d.js";


class Game
{
	id: number;
	players: Player[];
	resources: ResourceType[];
	board: Board;


	constructor(id: number, players: Player[], resources: ResourceType[], board: Board)
	{
		this.id = id;
		this.players = players;
		this.resources = resources;
		this.board = board;
	}
}
