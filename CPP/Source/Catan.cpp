/*
* @Author: MPZinke
* @Date:   2023-01-02 10:44:52
* @Last Modified by:   MPZinke
* @Last Modified time: 2023-01-12 22:04:06
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
	for(uint16_t x = 0; x < sizeof(HEXAGON_CORNERS)/sizeof(uint8_t[3]); x++)
	{
		uint16_t terrain_index = HEXAGON_CORNERS[x][0]-1;
		uint16_t corner_index = HEXAGON_CORNERS[x][1]-1;
		uint16_t hexagons_corner = HEXAGON_CORNERS[x][2];
		TERRAIN[terrain_index].corner(hexagons_corner, CORNERS[corner_index]);
	}

	for(uint16_t x = 0; x < sizeof(HEXAGON_EDGES)/sizeof(uint8_t[3]); x++)
	{
		uint16_t terrain_index = HEXAGON_EDGES[x][0]-1;
		uint16_t edge_index = HEXAGON_EDGES[x][1]-1;
		uint16_t hexagons_edge = HEXAGON_EDGES[x][2];
		TERRAIN[terrain_index].edge(hexagons_edge, EDGES[edge_index]);
	}

	for(uint16_t x = 0; x < sizeof(CORNER_EDGES)/sizeof(uint8_t[3]); x++)
	{
		uint16_t terrain_index = CORNER_EDGES[x][0]-1;
		uint16_t edge_index = CORNER_EDGES[x][1]-1;
		uint16_t corners_edge = CORNER_EDGES[x][2];
		TERRAIN[terrain_index].edge(corners_edge, EDGES[edge_index]);
	}
}


int main()
{
	associate_terrain();

	// desert.edge(Hexagon::Edges::TOP_LEFT, top_left1_bottom_right2);
	// top_left1_bottom_right2.hexagon(Edge::Hexagons::BOTTOM, desert);
	// wheat.edge(Hexagon::Edges::BOTTOM_RIGHT, top_left1_bottom_right2);
	// top_left1_bottom_right2.hexagon(Edge::Hexagons::TOP, wheat);

	// desert.corner(Hexagon::Corners::BOTTOM_LEFT);

	return 0;
}
