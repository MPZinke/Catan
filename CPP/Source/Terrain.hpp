

#include "Corner.hpp"
#include "Edge.hpp"
#include "Hexagon.hpp"
#include "ResourceType.hpp"





Hexagon TERRAIN[] = 
{
	Hexagon(1, WHEAT),
	Hexagon(2, WHEAT),
	Hexagon(3, WHEAT),
	Hexagon(4, WHEAT),
	Hexagon(5, WOOD),
	Hexagon(6, WOOD),
	Hexagon(7, WOOD),
	Hexagon(8, WOOD),
	Hexagon(9, SHEEP),
	Hexagon(10, SHEEP),
	Hexagon(11, SHEEP),
	Hexagon(12, SHEEP),
	Hexagon(13, STONE),
	Hexagon(14, STONE),
	Hexagon(15, STONE),
	Hexagon(16, BRICK),
	Hexagon(17, BRICK),
	Hexagon(18, BRICK),
	Hexagon(19, DESERT)
};


Corner CORNERS[] =
{
	Corner(1),
	Corner(2),
	Corner(3),
	Corner(4),
	Corner(5),
	Corner(6),
	Corner(7),
	Corner(8),
	Corner(9),
	Corner(10),
	Corner(11),
	Corner(12),
	Corner(13),
	Corner(14),
	Corner(15),
	Corner(16),
	Corner(17),
	Corner(18),
	Corner(19),
	Corner(20),
	Corner(21),
	Corner(22),
	Corner(23),
	Corner(24),
	Corner(25),
	Corner(26),
	Corner(27),
	Corner(28),
	Corner(29),
	Corner(30),
	Corner(31),
	Corner(32),
	Corner(33),
	Corner(34),
	Corner(35),
	Corner(36),
	Corner(37),
	Corner(38),
	Corner(39),
	Corner(40),
	Corner(41),
	Corner(42),
	Corner(43),
	Corner(44),
	Corner(45),
	Corner(46),
	Corner(47),
	Corner(48),
	Corner(49),
	Corner(50),
	Corner(51),
	Corner(52),
	Corner(53),
	Corner(54)
};


Edge EDGES[] =
{
	Edge(1),
};


uint8_t HEXAGON_CORNERS[][2] =  // {HexagonID, EdgeID}
{
	{1, 1},
	{1, 2},
	{1, 3},
	{1, 4},
	{1, 5},
	{1, 6},
};


uint8_t HEXAGON_EDGES[][2] =  // {HexagonID, EdgeID}
{
	{1, 1},
	{1, 2},
	{1, 3},
	{1, 4},
	{1, 5},
	{1, 6},
};
