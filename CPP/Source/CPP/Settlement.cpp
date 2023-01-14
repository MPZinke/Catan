
/***********************************************************************************************************************
*                                                                                                                      *
*   created by: MPZinke                                                                                                *
*   on 2023.01.09                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION: TEMPLATE                                                                                              *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


#include "Settlement.hpp"


#include "Corner.hpp"
#include "Hexagon.hpp"


Settlement::Settlement(uint16_t id)
: _id{id}
{}


// ———————————————————————————————————————————————————— GETTERS  ———————————————————————————————————————————————————— //

Corner* Settlement::corner()
{
	return _corner;
}


Player* Settlement::player()
{
	return _player;
}


// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

void Settlement::corner(Corner& corner)
{
	_corner = &corner;
}


void Settlement::corner(Corner* corner)
{
	_corner = corner;
}


void Settlement::player(Player& player)
{
	_player = &player;
}


void Settlement::player(Player* player)
{
	_player = player;
}


bool Settlement::is_blocked()
{
	for(uint16_t x = 0; x < Corner::Hexagons::HEXAGONS_LENGTH; x++)
	{
		if(_corner->hexagon(x) && _corner->hexagon(x)->robber())
		{
			return true;
		}
	}

	return false;
}