
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


#include <iostream>


#include "Hexagon.hpp"


#include "Association.hpp"
#include "Edge.hpp"


// FROM: https://stackoverflow.com/a/9282425
bool Hexagon::_visited_hexagons[NUMBER_OF_HEXAGONS];
std::vector<Hexagon*> Hexagon::_bfs_queue;


Hexagon::Hexagon(uint16_t id, ResourceType type, uint8_t value/*=0*/)
: _id{id}, _type{type}, _value{value}
{
	clear_bfs_data();
}


Hexagon::Hexagon(json& hexagon_data)
: _id{hexagon_data["id"]},
  _type{resource_type_for_name(hexagon_data["type"])},
  _value{static_cast<uint8_t>(hexagon_data.value("value", 0))}
{}


// ———————————————————————————————————————————————————— GETTERS  ———————————————————————————————————————————————————— //
// —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— //

// ————————————————————————————————————————————————— GETTERS::INFO  ————————————————————————————————————————————————— //

uint16_t Hexagon::id()
{
	return _id;
}


uint8_t Hexagon::type_for_name(std::string name)
{
	Association associations[] =
	{
		{Corners::BOTTOM_LEFT, "Hexagon::Corners::BOTTOM_LEFT"},
		{Corners::BOTTOM_RIGHT, "Hexagon::Corners::BOTTOM_RIGHT"},
		{Corners::RIGHT, "Hexagon::Corners::RIGHT"},
		{Corners::TOP_RIGHT, "Hexagon::Corners::TOP_RIGHT"},
		{Corners::TOP_LEFT, "Hexagon::Corners::TOP_LEFT"},
		{Corners::LEFT, "Hexagon::Corners::LEFT"},
		{Edges::BOTTOM, "Hexagon::Edges::BOTTOM"},
		{Edges::BOTTOM_RIGHT, "Hexagon::Edges::BOTTOM_RIGHT"},
		{Edges::TOP_RIGHT, "Hexagon::Edges::TOP_RIGHT"},
		{Edges::TOP, "Hexagon::Edges::TOP"},
		{Edges::TOP_LEFT, "Hexagon::Edges::TOP_LEFT"},
		{Edges::BOTTOM_LEFT, "Hexagon::Edges::BOTTOM_LEFT"},
	};

	return ::type_for_name(name, associations, Corners::CORNERS_LENGTH+Edges::EDGES_LENGTH);
}


ResourceType Hexagon::type()
{
	return _type;
}


uint8_t Hexagon::value()
{
	return _value;
}


// ————————————————————————————————————————————————— GETTERS::BOARD ————————————————————————————————————————————————— //

Corner* Hexagon::corner(uint16_t corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		
		std::exit(1);
	}

	return _corners[corner];
}


Edge* Hexagon::edge(uint16_t edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		
		std::exit(1);
	}

	return _edges[edge];
}


Hexagon* Hexagon::hexagon(uint16_t id)
{
	_visited_hexagons[_id] = true;


	if(_id == id)
	{
		clear_bfs_data();
		return this;
	}

	for(uint16_t x = 0; x < Edges::EDGES_LENGTH; x++)
	{
		if(_edges[x] == nullptr)
		{
			continue;
		}

		Hexagon* opposing_hexagon = *_edges[x] ^ this;
		if(Hexagon::can_be_enqueued(opposing_hexagon))
		{
			_bfs_queue.push_back(opposing_hexagon);
		}
	}

	Hexagon* next_hexagon = pop_bfs_queue();
	if(next_hexagon == nullptr)
	{
		clear_bfs_data();
		return nullptr;
	}
	return next_hexagon->hexagon(id);
}


Robber* Hexagon::robber()
{
	return _robber;
}


// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

void Hexagon::corner(uint16_t corner, Corner& new_corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		std::exit(1);
	}

	_corners[corner] = &new_corner;
}


void Hexagon::corner(uint16_t corner, Corner* new_corner)
{
	if(corner >= Corners::CORNERS_LENGTH)
	{
		std::exit(1);
	}

	_corners[corner] = new_corner;
}


void Hexagon::corner(std::string corner_label, Corner* new_corner)
{
	return corner(type_for_name(corner_label), new_corner);
}


void Hexagon::edge(uint16_t edge, Edge& new_edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	_edges[edge] = &new_edge;
}


void Hexagon::edge(uint16_t edge, Edge* new_edge)
{
	if(edge >= Edges::EDGES_LENGTH)
	{
		std::exit(1);
	}

	_edges[edge] = new_edge;
}


void Hexagon::edge(std::string edge_label, Edge* new_edge)
{
	return edge(type_for_name(edge_label), new_edge);
}


void Hexagon::robber(Robber& robber)
{
	_robber = &robber;
}


void Hexagon::robber(Robber* robber)
{
	_robber = robber;
}


// ————————————————————————————————————————————————————— STATIC ————————————————————————————————————————————————————— //

bool Hexagon::can_be_enqueued(Hexagon* hexagon)
{
	if(hexagon == nullptr)
	{
		return false;
	}

	if(_visited_hexagons[hexagon->id()] == true)
	{
		return false;
	}

	for(uint16_t x = 0; x < _bfs_queue.size(); x++)
	{
		if(hexagon == _bfs_queue[x])
		{
			return false;
		}
	}

	return true;
}


void Hexagon::clear_bfs_data()
{
	_bfs_queue.clear();
	std::fill(_visited_hexagons, _visited_hexagons + NUMBER_OF_HEXAGONS, false);
}


Hexagon* Hexagon::pop_bfs_queue()
{
	if(_bfs_queue.size() == 0)
	{
		return nullptr;
	}

	Hexagon* head = _bfs_queue[0];
	_bfs_queue.erase(_bfs_queue.begin());
	return head;
}
