
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


Edge::Edge(json& edge_data)
: _id{edge_data["id"]}
{}


// ———————————————————————————————————————————————————— GETTERS  ———————————————————————————————————————————————————— //
// —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— //

// ————————————————————————————————————————————————— GETTERS::INFO  ————————————————————————————————————————————————— //

uint16_t Edge::id()
{
	return _id;
}


// ————————————————————————————————————————————————— GETTERS::BOARD ————————————————————————————————————————————————— //

Corner* Edge::corner(uint16_t corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		exit(1);
	}

	return _corners[corner];
}


Hexagon* Edge::hexagon(uint16_t hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	return _hexagons[hexagon];
}


Hexagon* Edge::operator^(Hexagon* hexagon)
{
	return _hexagons[hexagon == _hexagons[Hexagons::BOTTOM]];
}



// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

void Edge::corner(uint16_t corner, Corner& new_corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		exit(1);
	}

	_corners[corner] = &new_corner;
}


void Edge::hexagon(uint16_t hexagon, Hexagon& new_hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	_hexagons[hexagon] = &new_hexagon;
}
