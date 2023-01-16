

#include "Corner.hpp"


#include <iostream>


Corner::Corner(uint16_t id)
: _id{id}
{}


Corner::Corner(json& corner_data)
: _id{corner_data["id"]}
{}


// ———————————————————————————————————————————————————— GETTERS  ———————————————————————————————————————————————————— //
// —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— //

// ————————————————————————————————————————————————— GETTERS::INFO  ————————————————————————————————————————————————— //

uint16_t Corner::id()
{
	return _id;
}


// ————————————————————————————————————————————————— GETTERS::BOARD ————————————————————————————————————————————————— //

Edge* Corner::edge(uint16_t edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	return _edges[edge];
}


Hexagon* Corner::hexagon(uint16_t hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		exit(1);
	}

	return _hexagons[hexagon];
}


// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

void Corner::edge(uint16_t edge, Edge& new_edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	_edges[edge] = &new_edge;
}


void Corner::edge(uint16_t edge, Edge* new_edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	_edges[edge] = new_edge;
}


void Corner::hexagon(uint16_t hexagon, Hexagon& new_hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		std::exit(1);
	}

	_hexagons[hexagon] = &new_hexagon;
}


void Corner::hexagon(uint16_t hexagon, Hexagon* new_hexagon)
{
	if(hexagon >= Hexagons::HEXAGONS_LENGTH)
	{
		std::exit(1);
	}

	_hexagons[hexagon] = new_hexagon;
}
