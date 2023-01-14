
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


#include "Edge.hpp"
#include "Hexagon.hpp"


#include <iostream>


// FROM: https://stackoverflow.com/a/9282425
bool Hexagon::_visited_hexagons[NUMBER_OF_HEXAGONS];
std::vector<Hexagon*> Hexagon::_bfs_queue;


Hexagon::Hexagon(uint16_t id, ResourceType type, uint8_t value/*=0*/)
: _id{id}, _type{type}, _value{value}
{
	clear_bfs_data();
}


// ———————————————————————————————————————————————————— GETTERS  ———————————————————————————————————————————————————— //

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
		if(Hexagon::can_be_queued(opposing_hexagon))
		{
			_bfs_queue.push_back(opposing_hexagon);
		}
	}

	Hexagon* next_hexagon = pop_bfs_queue();
	std::cout << _id << std::endl;
	return next_hexagon != nullptr ? next_hexagon->hexagon(id) : nullptr;
}


uint16_t Hexagon::id()
{
	return _id;
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


// ————————————————————————————————————————————————————— STATIC ————————————————————————————————————————————————————— //

bool Hexagon::can_be_queued(Hexagon* hexagon)
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

	for(uint16_t x = 0; x < NUMBER_OF_HEXAGONS; x++)
	{
		_visited_hexagons[x] = false;
	}
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
