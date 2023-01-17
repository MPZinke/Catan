
/***********************************************************************************************************************
*                                                                                                                      *
*   created by: MPZinke                                                                                                *
*   on 2023.01.02                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION: TEMPLATE                                                                                              *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


#include <iostream>


#include "Corner.hpp"
#include "Edge.hpp"
#include "Game.hpp"
#include "Hexagon.hpp"
#include "Player.hpp"
#include "ResourceType.hpp"
#include "Settlement.hpp"


int main()
{
	Game game("GameData.json");
	game.hexagon(0)->hexagon(15);

	return 0;
}
