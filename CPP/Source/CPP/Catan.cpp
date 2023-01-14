/*
* @Author: MPZinke
* @Date:   2023-01-02 10:44:52
* @Last Modified by:   MPZinke
* @Last Modified time: 2023-01-13 17:40:37
*/


#include <iostream>


#include "Board.hpp"
#include "Corner.hpp"
#include "Edge.hpp"
#include "Hexagon.hpp"
#include "Player.hpp"
#include "ResourceType.hpp"
#include "Settlement.hpp"


int main()
{
	associate_terrain();

	Hexagon* hexagon0 = EDGES[0].hexagon(Hexagon::Edges::BOTTOM);
	Hexagon* hexagon1 = EDGES[0].hexagon(Edge::Hexagons::TOP);
	std::cout << "Hexagon0: " << (hexagon0 ? "True" : "False") << std::endl;
	std::cout << "Hexagon1: " << (hexagon1 ? "True" : "False") << std::endl;

	std::cout << "HEXAGONS[9].hexagon(19): " << HEXAGONS[9].hexagon(19) << std::endl;

	return 0;
}
