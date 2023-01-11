
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


#include "Hexagon.hpp"


#include <iostream>


Hexagon::Hexagon(uint16_t id, ResourceType type, uint8_t value/*=0*/)
: _id{id}, _type{type}, _value{value}
{}


// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

Corner& Hexagon::corner(Corners::Corner corner)
{
	if(corner < Corners::CORNERS_LENGTH)
	{
		std::exit(1);
	}

	return *_corners[corner];
}


Edge& Hexagon::edge(Edges::Edge edge)
{
	if(edge < Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	return *_edges[edge];
}


ResourceType Hexagon::type()
{
	return _type;
}


uint8_t Hexagon::value()
{
	return _value;
}


// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

void Hexagon::corner(Corners::Corner corner, Corner& new_corner)
{
	if(corner < Corners::CORNERS_LENGTH)
	{
		std::exit(1);
	}

	_corners[corner] = &new_corner;
}


void Hexagon::edge(Edges::Edge edge, Edge& new_edge)
{
	if(edge < Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	_edges[edge] = &new_edge;
}
