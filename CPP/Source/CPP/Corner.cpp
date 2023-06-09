

#include "Corner.hpp"


#include <iostream>


#include "Association.hpp"


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


uint8_t Corner::type_for_label(std::string label)
{
	Association associations[] =
	{
		{Edges::BOTTOM, "Corner::Edges::BOTTOM"},
		{Edges::TOP, "Corner::Edges::TOP"},
		{Edges::SIDE, "Corner::Edges::SIDE"},
		{Hexagons::BOTTOM, "Corner::Hexagons::BOTTOM"},
		{Hexagons::TOP, "Corner::Hexagons::TOP"},
		{Hexagons::SIDE, "Corner::Hexagons::SIDE"}
	};

	return ::type_for_label(label, associations, Edges::EDGES_LENGTH+Hexagons::HEXAGONS_LENGTH);
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


Port* Corner::port()
{
	return _port;
}


Settlement* Corner::settlement()
{
	return _settlement;
}


// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

void Corner::edge(uint16_t edge, Edge* new_edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	_edges[edge] = new_edge;
}


void Corner::edge(std::string edge_label, Edge* new_edge)
{
	return edge(type_for_label(edge_label), new_edge);
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


void Corner::hexagon(std::string hexagon_label, Hexagon* new_hexagon)
{
	return hexagon(type_for_label(hexagon_label), new_hexagon);
}
