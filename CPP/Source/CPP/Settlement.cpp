
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


Settlement::Settlement(uint16_t id, Player* player, Corner* corner)
: _id{id}, _player{player}, _corner{corner}
{}


// ———————————————————————————————————————————————————— GETTERS  ———————————————————————————————————————————————————— //

uint16_t Settlement::id()
{
	return _id;
}


Corner* Settlement::corner()
{
	return (Corner*)_corner;
}


Player* Settlement::player()
{
	return (Player*)_player;
}


Settlement::Type Settlement::type()
{
	return _type;
}


// —————————————————————————————————————————————————————— GAME —————————————————————————————————————————————————————— //

bool Settlement::is_blocked()
{
	for(uint16_t x = 0; x < Corner::Hexagons::HEXAGONS_LENGTH; x++)
	{
		Corner& corner = (Corner&)_corner;
		if(corner.hexagon(x) && corner.hexagon(x)->robber())
		{
			return true;
		}
	}

	return false;
}


bool Settlement::upgrade()
{
	if(_type != VILLAGE)
	{
		return false;
	}

	_type = CITY;
	return true;
}