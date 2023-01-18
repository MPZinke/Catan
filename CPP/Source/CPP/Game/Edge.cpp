
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


#include "Association.hpp"


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


uint8_t Edge::type_for_label(std::string label)
{
	Association associations[] =
	{
		{Corners::LEFT, "Edge::Corners::LEFT"},
		{Corners::RIGHT, "Edge::Corners::RIGHT"},
		{Hexagons::BOTTOM, "Edge::Hexagons::BOTTOM"},
		{Hexagons::TOP, "Edge::Hexagons::TOP"},
	};

	return ::type_for_label(label, associations, Corners::CORNERS_LENGTH+Hexagons::HEXAGONS_LENGTH);
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


void Edge::corner(uint16_t corner, Corner* new_corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		exit(1);
	}

	_corners[corner] = new_corner;
}


void Edge::corner(std::string corner_label, Corner* new_corner)
{
	return corner(type_for_label(corner_label), new_corner);
}


void Edge::hexagon(uint16_t hexagon, Hexagon& new_hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	_hexagons[hexagon] = &new_hexagon;
}


void Edge::hexagon(uint16_t hexagon, Hexagon* new_hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	_hexagons[hexagon] = new_hexagon;
}


void Edge::hexagon(std::string hexagon_label, Hexagon* new_hexagon)
{
	return hexagon(type_for_label(hexagon_label), new_hexagon);
}
