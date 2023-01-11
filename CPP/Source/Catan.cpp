/*
* @Author: MPZinke
* @Date:   2023-01-02 10:44:52
* @Last Modified by:   MPZinke
* @Last Modified time: 2023-01-02 11:15:58
*/


#include "Corner.hpp"
#include "Edge.hpp"
#include "Hexagon.hpp"
#include "ResourceType.hpp"
#include "Settlement.hpp"


int main()
{
	Hexagon desert(1, DESERT);
	Edge top_left1_bottom_right2(1);

	desert.corner(Hexagon::Corners::BOTTOM_LEFT);

	return 0;
}
