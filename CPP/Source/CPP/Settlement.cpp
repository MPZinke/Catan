
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


Settlement::Settlement(uint16_t id)
: _id{id}
{}


void Settlement::corner(Corner* corner)
{
	_corner = corner;
}


Corner* Settlement::corner()
{
	return _corner;
}


void Settlement::player(Player* player)
{
	_player = player;
}


Player* Settlement::player()
{
	return _player;
}
