

#include <stdint.h>


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
	Edge(2),
	Edge(3),
	Edge(4),
	Edge(5),
	Edge(6),
	Edge(7),
	Edge(8),
	Edge(9),
	Edge(10),
	Edge(11),
	Edge(12),
	Edge(13),
	Edge(14),
	Edge(15),
	Edge(16),
	Edge(17),
	Edge(18),
	Edge(19),
	Edge(20),
	Edge(21),
	Edge(22),
	Edge(23),
	Edge(24),
	Edge(25),
	Edge(26),
	Edge(27),
	Edge(28),
	Edge(29),
	Edge(30),
	Edge(31),
	Edge(32),
	Edge(33),
	Edge(34),
	Edge(35),
	Edge(36),
	Edge(37),
	Edge(38),
	Edge(39),
	Edge(40),
	Edge(41),
	Edge(42),
	Edge(43),
	Edge(44),
	Edge(45),
	Edge(46),
	Edge(47),
	Edge(48),
	Edge(49),
	Edge(50),
	Edge(51),
	Edge(52),
	Edge(53),
	Edge(54),
	Edge(55),
	Edge(56),
	Edge(57),
	Edge(58),
	Edge(59),
	Edge(60),
	Edge(61),
	Edge(62),
	Edge(63),
	Edge(64),
	Edge(65),
	Edge(66),
	Edge(67),
	Edge(68),
	Edge(69),
	Edge(70),
	Edge(71),
	Edge(72)
};


uint8_t HEXAGON_CORNERS[][4] =  // {HexagonID, EdgeID, Corner relative to hexagon, Hexagon relative to corner}
{
	{1, 1, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{1, 2, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{1, 5, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{1, 10, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{1, 9, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{1, 4, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},
	
	{2, 3, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{2, 4, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{2, 9, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{2, 15, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{2, 14, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{2, 8, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{3, 5, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{3, 6, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{3, 11, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{3, 17, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{3, 16, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{3, 10, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{4, 7, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{4, 8, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{4, 14, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{4, 20, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{4, 19, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{4, 13, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{5, 9, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{5, 10, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{5, 16, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{5, 22, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{5, 21, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{5, 15, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{6, 11, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{6, 12, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{6, 18, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{6, 24, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{6, 23, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{6, 17, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{7, 14, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{7, 15, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{7, 21, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{7, 27, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{7, 26, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{7, 20, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{8, 16, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{8, 17, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{8, 23, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{8, 29, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{8, 28, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{8, 22, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{9, 19, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{9, 20, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{9, 26, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{9, 32, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{9, 31, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{9, 25, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{10, 21, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{10, 22, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{10, 28, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{10, 34, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{10, 33, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{10, 27, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{11, 23, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{11, 24, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{11, 30, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{11, 36, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{11, 35, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{11, 29, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{12, 26, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{12, 27, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{12, 33, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{12, 39, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{12, 38, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{12, 32, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{13, 28, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{13, 29, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{13, 35, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{13, 41, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{13, 40, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{13, 34, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{14, 31, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{14, 32, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{14, 38, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{14, 44, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{14, 43, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{14, 37, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{15, 33, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{15, 34, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{15, 40, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{15, 46, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{15, 45, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{15, 39, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{16, 35, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{16, 36, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{16, 42, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{16, 48, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{16, 47, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{16, 41, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{17, 38, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{17, 39, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{17, 45, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{17, 50, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{17, 49, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{17, 44, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{18, 40, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{18, 41, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{18, 47, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{18, 52, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{18, 51, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{18, 46, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{19, 45, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{19, 46, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{19, 51, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{19, 54, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{19, 53, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{19, 50, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE}
};


uint8_t HEXAGON_EDGES[][4] =  // {HexagonID, EdgeID, Corner relative to hexagon, Hexagon relative to corner}
{
	{1, 1, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{1, 3, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{1, 8, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{1, 11, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{1, 7, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{1, 2, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{2, 4, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{2, 7, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{2, 15, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{2, 19, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{2, 14, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{2, 6, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{3, 5, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{3, 9, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{3, 17, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{3, 20, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{3, 16, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{3, 8, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{4, 10, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{4, 14, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{4, 22, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{4, 27, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{4, 21, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{4, 13, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{5, 11, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{5, 16, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{5, 24, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{5, 28, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{5, 23, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{5, 15, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{6, 12, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{6, 18, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{6, 26, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{6, 29, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{6, 25, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{6, 17, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{7, 19, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{7, 23, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{7, 32, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{7, 36, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{7, 31, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{7, 22, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{8, 20, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{8, 25, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{8, 34, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{8, 37, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{8, 33, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{8, 24, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{9, 27, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{9, 31, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{9, 39, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{9, 44, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{9, 38, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{9, 30, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{10, 28, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{10, 33, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{10, 41, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{10, 45, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{10, 40, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{10, 32, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{11, 29, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{11, 35, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{11, 43, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{11, 46, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{11, 42, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{11, 34, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{12, 36, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{12, 40, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{12, 49, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{12, 53, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{12, 48, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{12, 39, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{13, 37, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{13, 42, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{13, 51, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{13, 54, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{13, 50, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{13, 41, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{14, 44, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{14, 48, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{14, 56, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{14, 61, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{14, 55, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{14, 47, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{15, 45, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{15, 50, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{15, 58, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{15, 62, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{15, 57, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{15, 49, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{16, 46, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{16, 52, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{16, 60, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{16, 63, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{16, 59, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{16, 51, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{17, 53, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{17, 57, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{17, 65, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{17, 68, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{17, 64, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{17, 56, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{18, 54, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{18, 59, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{18, 67, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{18, 69, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{18, 66, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{18, 58, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{19, 62, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{19, 66, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{19, 71, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{19, 72, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{19, 70, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{19, 65, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP}
};


uint8_t CORNER_EDGES[][4] =  // {CornerID, EdgeID, Corner relative to hexagon, Hexagon relative to corner}
{
	{1, 1, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{1, 2, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{2, 1, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{2, 3, Corner::Edges::TOP, Edge::Corners::LEFT},

	{3, 4, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{3, 6, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{4, 2, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{4, 4, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{4, 7, Corner::Edges::TOP, Edge::Corners::LEFT},

	{5, 3, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{5, 5, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{5, 8, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{6, 5, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{6, 9, Corner::Edges::TOP, Edge::Corners::LEFT},

	{7, 10, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{7, 13, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{8, 6, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{8, 10, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{8, 14, Corner::Edges::TOP, Edge::Corners::LEFT},

	{9, 7, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{9, 11, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{9, 15, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{10, 8, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{10, 11, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{10, 16, Corner::Edges::TOP, Edge::Corners::LEFT},

	{11, 9, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{11, 12, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{11, 17, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{12, 12, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{12, 18, Corner::Edges::TOP, Edge::Corners::LEFT},

	{13, 13, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{13, 21, Corner::Edges::TOP, Edge::Corners::LEFT},

	{14, 14, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{14, 19, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{14, 22, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{15, 15, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{15, 19, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{15, 23, Corner::Edges::TOP, Edge::Corners::LEFT},

	{16, 16, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{16, 20, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{16, 24, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{17, 17, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{17, 20, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{17, 25, Corner::Edges::TOP, Edge::Corners::LEFT},

	{18, 18, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{18, 26, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{19, 21, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{19, 27, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{19, 30, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{20, 22, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{20, 27, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{20, 31, Corner::Edges::TOP, Edge::Corners::LEFT},

	{21, 23, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{21, 28, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{21, 32, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{22, 24, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{22, 28, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{22, 33, Corner::Edges::TOP, Edge::Corners::LEFT},

	{23, 25, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{23, 29, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{23, 42, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{24, 26, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{24, 29, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{24, 35, Corner::Edges::TOP, Edge::Corners::LEFT},

	{25, 30, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{25, 38, Corner::Edges::TOP, Edge::Corners::LEFT},

	{26, 31, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{26, 36, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{26, 39, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{27, 32, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{27, 36, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{27, 40, Corner::Edges::TOP, Edge::Corners::LEFT},

	{28, 33, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{28, 37, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{28, 41, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{29, 34, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{29, 37, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{29, 42, Corner::Edges::TOP, Edge::Corners::LEFT},

	{30, 35, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{30, 43, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{31, 38, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{31, 44, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{31, 47, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{32, 39, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{32, 44, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{32, 48, Corner::Edges::TOP, Edge::Corners::LEFT},

	{33, 40, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{33, 45, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{33, 49, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{34, 41, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{34, 45, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{34, 50, Corner::Edges::TOP, Edge::Corners::LEFT},

	{35, 42, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{35, 46, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{35, 51, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{36, 43, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{36, 46, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{36, 52, Corner::Edges::TOP, Edge::Corners::LEFT},

	{37, 47, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{37, 48, Corner::Edges::TOP, Edge::Corners::LEFT},

	{38, 48, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{38, 53, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{38, 56, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{39, 49, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{39, 53, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{39, 57, Corner::Edges::TOP, Edge::Corners::LEFT},

	{40, 50, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{40, 54, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{40, 58, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{41, 51, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{41, 54, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{41, 59, Corner::Edges::TOP, Edge::Corners::LEFT},

	{42, 52, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{42, 60, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{43, 55, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{43, 61, Corner::Edges::SIDE, Edge::Corners::LEFT},

	{44, 56, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{44, 61, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{44, 64, Corner::Edges::TOP, Edge::Corners::LEFT},

	{45, 57, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{45, 62, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{45, 65, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{46, 58, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{46, 62, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{46, 66, Corner::Edges::TOP, Edge::Corners::LEFT},

	{47, 59, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{47, 63, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{47, 67, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{48, 60, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{48, 63, Corner::Edges::SIDE, Edge::Corners::RIGHT},

	{49, 64, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{49, 68, Corner::Edges::SIDE, Edge::Corners::LEFT},

	{50, 65, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{50, 68, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{50, 70, Corner::Edges::TOP, Edge::Corners::LEFT},

	{51, 66, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{51, 69, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{51, 71, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{52, 67, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{52, 69, Corner::Edges::SIDE, Edge::Corners::RIGHT},

	{53, 70, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{53, 72, Corner::Edges::SIDE, Edge::Corners::LEFT},

	{54, 71, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{54, 72, Corner::Edges::SIDE, Edge::Corners::RIGHT}
};
