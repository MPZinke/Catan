
/***********************************************************************************************************************
*                                                                                                                      *
*   created by: MPZinke                                                                                                *
*   on 2023.01.11                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION: TEMPLATE                                                                                              *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


#include "Edge.hpp"


#include <iostream>


Edge::Edge(uint16_t id)
: _id{id}
{}

// ———— GETTERS ———— //
Corner& Edge::corner(Corners::Corner corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		exit(1);
	}

	return *_corners[corner];
}


Hexagon& Edge::hexagon(Hexagons::Hexagon hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	return *_hexagons[hexagon];
}


// ———— SETTERS ———— //
void Edge::corner(Corners::Corner corner, Corner& new_corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		exit(1);
	}

	_corners[corner] = &new_corner;
}


void Edge::hexagon(Hexagons::Hexagon hexagon, Hexagon& new_hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	_hexagons[hexagon] = &new_hexagon;
}
