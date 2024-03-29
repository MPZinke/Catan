
/***********************************************************************************************************************
*                                                                                                                      *
*   created by: MPZinke                                                                                                *
*   on 2023.01.15                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION: TEMPLATE                                                                                              *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


#include <fstream>
#include <iostream>


#include "Game.hpp"


Game::Game(std::string filename)
{
	using namespace nlohmann;

	std::ifstream file(filename);
	json game_data = json::parse(file);

	for(json& corner_data : game_data["Corners"])
	{
		_corners.push_back(new Corner(corner_data));
	}

	for(json& edge_data : game_data["Edges"])
	{
		_edges.push_back(new Edge(edge_data));
	}

	for(json& hexagon_data : game_data["Hexagons"])
	{
		_hexagons.push_back(new Hexagon(hexagon_data));
	}

	for(json& port_data : game_data["Ports"])
	{
		// _ports.push_back(new Port(port_data));
	}

	associate_parts(game_data);
}


void Game::associate_parts(json& game_data)
{
	associate_corner_with_parts(game_data);
	associate_edge_with_parts(game_data);
	associate_hexagon_with_parts(game_data);
}


void Game::associate_corner_with_parts(json& game_data)
{
	for(json& corner_data : game_data["Corners"])
	{
		Corner* corner = this->corner(corner_data["id"]);

		for(auto& corners_edge : corner_data["Edges"].items())
		{
			Edge* edge = this->edge(corners_edge.value());
			corner->edge(corners_edge.key(), edge);
		}

		for(auto& corners_hexagon : corner_data["Hexagons"].items())
		{
			Hexagon* hexagon = this->hexagon(corners_hexagon.value());
			corner->hexagon(corners_hexagon.key(), hexagon);
		}
	}
}


void Game::associate_edge_with_parts(json& game_data)
{
	for(json& edge_data : game_data["Edges"])
	{
		Edge* edge = this->edge(edge_data["id"]);

		for(auto& edges_corner : edge_data["Corners"].items())
		{
			Corner* corner = this->corner(edges_corner.value());
			edge->corner(edges_corner.key(), corner);
		}

		for(auto& edges_hexagon : edge_data["Hexagons"].items())
		{
			Hexagon* hexagon = this->hexagon(edges_hexagon.value());
			edge->hexagon(edges_hexagon.key(), hexagon);
		}
	}
}


void Game::associate_hexagon_with_parts(json& game_data)
{
	for(json& hexagon_data : game_data["Hexagons"])
	{
		Hexagon* hexagon = this->hexagon(hexagon_data["id"]);

		for(auto& hexagons_corner : hexagon_data["Corners"].items())
		{
			Corner* corner = this->corner(hexagons_corner.value());
			hexagon->corner(hexagons_corner.key(), corner);
		}

		for(auto& hexagons_edge : hexagon_data["Edges"].items())
		{
			Edge* edge = this->edge(hexagons_edge.value());
			hexagon->edge(hexagons_edge.key(), edge);
		}
	}
}


Corner* Game::corner(uint16_t id)
{
	for(uint16_t x = 0; x < _corners.size(); x++)
	{
		Corner* corner = _corners[x];
		if(corner->id() == id)
		{
			return _corners[x];
		}
	}

	return nullptr;
}


Edge* Game::edge(uint16_t id)
{
	for(uint16_t x = 0; x < _edges.size(); x++)
	{
		Edge* edge = _edges[x];
		if(edge->id() == id)
		{
			return _edges[x];
		}
	}

	return nullptr;
}


Hexagon* Game::hexagon(uint16_t id)
{
	for(uint16_t x = 0; x < _hexagons.size(); x++)
	{
		Hexagon* hexagon = _hexagons[x];
		if(hexagon->id() == id)
		{
			return _hexagons[x];
		}
	}

	return nullptr;
}
