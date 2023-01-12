

#include "Corner.hpp"


#include <iostream>


Corner::Corner(uint16_t id)
: _id{id}
{}


Edge& Corner::edge(Edges::Edge edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	return *_edges[edge];
}


Hexagon& Corner::hexagon(Hexagons::Hexagon hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	return *_hexagons[hexagon];
}
