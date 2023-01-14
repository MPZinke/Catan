/*
* @Author: MPZinke
* @Date:   2023-01-02 10:44:52
* @Last Modified by:   MPZinke
* @Last Modified time: 2023-01-13 17:40:37
*/


#include <iostream>


#include "Corner.hpp"
#include "Edge.hpp"
#include "Hexagon.hpp"
#include "ResourceType.hpp"
#include "Terrain.hpp"
#include "Settlement.hpp"


void associate_terrain()
{
	for(uint16_t x = 0; x < sizeof(HEXAGON_CORNERS)/sizeof(uint8_t[4]); x++)
	{
		uint16_t hexagon_index = HEXAGON_CORNERS[x][0]-1;
		uint16_t corner_index = HEXAGON_CORNERS[x][1]-1;
		uint16_t hexagons_corner = HEXAGON_CORNERS[x][2];
		uint16_t corners_hexagon = HEXAGON_CORNERS[x][3];
		TERRAIN[hexagon_index].corner(hexagons_corner, CORNERS[corner_index]);
		CORNERS[corner_index].hexagon(corners_hexagon, TERRAIN[hexagon_index]);
	}

	for(uint16_t x = 0; x < sizeof(HEXAGON_EDGES)/sizeof(uint8_t[4]); x++)
	{
		uint16_t hexagon_index = HEXAGON_EDGES[x][0]-1;
		uint16_t edge_index = HEXAGON_EDGES[x][1]-1;
		uint16_t hexagons_edge = HEXAGON_EDGES[x][2];
		uint16_t edges_hexagon = HEXAGON_EDGES[x][3];
		TERRAIN[hexagon_index].edge(hexagons_edge, EDGES[edge_index]);
		EDGES[edge_index].hexagon(edges_hexagon, TERRAIN[hexagon_index]);
	}

	for(uint16_t x = 0; x < sizeof(CORNER_EDGES)/sizeof(uint8_t[4]); x++)
	{
		uint16_t corner_index = CORNER_EDGES[x][0]-1;
		uint16_t edge_index = CORNER_EDGES[x][1]-1;
		uint16_t corners_edge = CORNER_EDGES[x][2];
		uint16_t edges_corner = HEXAGON_EDGES[x][3];
		CORNERS[corner_index].edge(corners_edge, EDGES[edge_index]);
		EDGES[edge_index].corner(edges_corner, CORNERS[corner_index]);
	}
}


int main()
{
	associate_terrain();

	Hexagon* hexagon0 = EDGES[0].hexagon(Hexagon::Edges::BOTTOM);
	Hexagon* hexagon1 = EDGES[0].hexagon(Edge::Hexagons::TOP);
	std::cout << "Hexagon0: " << (hexagon0 ? "True" : "False") << std::endl;
	std::cout << "Hexagon1: " << (hexagon1 ? "True" : "False") << std::endl;

	std::cout << "TERRAIN[0].hexagon(4): " << TERRAIN[0].hexagon(4) << std::endl;

	return 0;
}
