

#include "Board.hpp"


Hexagon HEXAGONS[] = 
{
	Hexagon(0, WHEAT),
	Hexagon(1, WHEAT),
	Hexagon(2, WHEAT),
	Hexagon(3, WHEAT),
	Hexagon(4, WOOD),
	Hexagon(5, WOOD),
	Hexagon(6, WOOD),
	Hexagon(7, WOOD),
	Hexagon(8, SHEEP),
	Hexagon(9, SHEEP),
	Hexagon(10, SHEEP),
	Hexagon(11, SHEEP),
	Hexagon(12, STONE),
	Hexagon(13, STONE),
	Hexagon(14, STONE),
	Hexagon(15, BRICK),
	Hexagon(16, BRICK),
	Hexagon(17, BRICK),
	Hexagon(18, DESERT)
};


Corner CORNERS[] =
{
	Corner(0),
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
	Corner(53)
};


Edge EDGES[] =
{
	Edge(0),
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
	Edge(71)
};


uint8_t HEXAGON_CORNERS[][4] =  // {HexagonID, EdgeID, Corner relative to hexagon, Hexagon relative to corner}
{
	{0, 0, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{0, 1, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{0, 4, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{0, 9, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{0, 8, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{0, 3, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},
	
	{1, 2, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{1, 3, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{1, 8, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{1, 14, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{1, 13, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{1, 7, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{2, 4, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{2, 5, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{2, 10, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{2, 16, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{2, 15, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{2, 9, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{3, 6, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{3, 7, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{3, 13, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{3, 19, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{3, 18, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{3, 12, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{4, 8, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{4, 9, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{4, 15, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{4, 21, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{4, 20, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{4, 14, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{5, 10, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{5, 11, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{5, 17, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{5, 23, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{5, 22, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{5, 16, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{6, 13, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{6, 14, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{6, 20, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{6, 26, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{6, 25, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{6, 19, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{7, 15, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{7, 16, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{7, 22, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{7, 28, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{7, 27, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{7, 21, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{8, 18, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{8, 19, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{8, 25, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{8, 31, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{8, 30, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{8, 24, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{9, 20, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{9, 21, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{9, 27, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{9, 33, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{9, 32, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{9, 26, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{10, 22, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{10, 23, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{10, 29, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{10, 35, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{10, 34, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{10, 28, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{11, 25, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{11, 26, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{11, 32, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{11, 38, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{11, 37, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{11, 31, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{12, 27, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{12, 28, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{12, 34, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{12, 40, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{12, 39, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{12, 33, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{13, 30, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{13, 31, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{13, 37, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{13, 43, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{13, 42, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{13, 36, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{14, 32, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{14, 33, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{14, 39, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{14, 45, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{14, 44, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{14, 38, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{15, 34, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{15, 35, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{15, 41, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{15, 47, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{15, 46, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{15, 40, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{16, 37, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{16, 38, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{16, 44, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{16, 49, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{16, 48, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{16, 43, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{17, 39, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{17, 40, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{17, 46, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{17, 51, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{17, 50, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{17, 45, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE},

	{18, 44, Hexagon::Corners::BOTTOM_LEFT, Corner::Hexagons::TOP},
	{18, 45, Hexagon::Corners::BOTTOM_RIGHT, Corner::Hexagons::TOP},
	{18, 50, Hexagon::Corners::RIGHT, Corner::Hexagons::SIDE},
	{18, 53, Hexagon::Corners::TOP_RIGHT, Corner::Hexagons::BOTTOM},
	{18, 52, Hexagon::Corners::TOP_LEFT, Corner::Hexagons::BOTTOM},
	{18, 49, Hexagon::Corners::LEFT, Corner::Hexagons::SIDE}
};


uint8_t HEXAGON_EDGES[][4] =  // {HexagonID, EdgeID, Corner relative to hexagon, Hexagon relative to corner}
{
	{0, 0, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{0, 2, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{0, 7, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{0, 10, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{0, 6, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{0, 1, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{1, 3, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{1, 6, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{1, 14, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{1, 18, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{1, 13, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{1, 5, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{2, 4, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{2, 8, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{2, 16, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{2, 19, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{2, 15, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{2, 7, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{3, 9, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{3, 13, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{3, 21, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{3, 26, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{3, 20, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{3, 12, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{4, 10, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{4, 15, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{4, 23, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{4, 27, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{4, 22, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{4, 14, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{5, 11, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{5, 17, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{5, 25, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{5, 28, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{5, 24, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{5, 16, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{6, 18, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{6, 22, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{6, 31, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{6, 35, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{6, 30, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{6, 21, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{7, 19, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{7, 24, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{7, 33, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{7, 36, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{7, 32, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{7, 23, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{8, 26, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{8, 30, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{8, 38, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{8, 43, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{8, 37, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{8, 29, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{9, 27, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{9, 32, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{9, 40, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{9, 44, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{9, 39, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{9, 31, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{10, 28, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{10, 34, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{10, 42, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{10, 45, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{10, 41, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{10, 33, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{11, 35, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{11, 39, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{11, 48, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{11, 52, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{11, 47, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{11, 38, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{12, 36, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{12, 41, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{12, 50, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{12, 53, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{12, 49, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{12, 40, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{13, 43, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{13, 47, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{13, 55, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{13, 60, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{13, 54, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{13, 46, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{14, 44, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{14, 49, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{14, 57, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{14, 61, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{14, 56, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{14, 48, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{15, 45, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{15, 51, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{15, 59, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{15, 62, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{15, 58, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{15, 50, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{16, 52, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{16, 56, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{16, 64, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{16, 67, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{16, 63, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{16, 55, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{17, 53, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{17, 58, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{17, 66, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{17, 68, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{17, 65, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{17, 57, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP},

	{18, 61, Hexagon::Edges::BOTTOM, Edge::Hexagons::TOP},
	{18, 65, Hexagon::Edges::BOTTOM_RIGHT, Edge::Hexagons::TOP},
	{18, 70, Hexagon::Edges::TOP_RIGHT, Edge::Hexagons::BOTTOM},
	{18, 71, Hexagon::Edges::TOP, Edge::Hexagons::BOTTOM},
	{18, 69, Hexagon::Edges::TOP_LEFT, Edge::Hexagons::BOTTOM},
	{18, 64, Hexagon::Edges::BOTTOM_LEFT, Edge::Hexagons::TOP}
};


uint8_t CORNER_EDGES[][4] =  // {CornerID, EdgeID, Corner relative to hexagon, Hexagon relative to corner}
{
	{0, 0, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{0, 1, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{1, 0, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{1, 2, Corner::Edges::TOP, Edge::Corners::LEFT},

	{2, 3, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{2, 5, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{3, 1, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{3, 3, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{3, 6, Corner::Edges::TOP, Edge::Corners::LEFT},

	{4, 2, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{4, 4, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{4, 7, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{5, 4, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{5, 8, Corner::Edges::TOP, Edge::Corners::LEFT},

	{6, 9, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{6, 12, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{7, 5, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{7, 9, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{7, 13, Corner::Edges::TOP, Edge::Corners::LEFT},

	{8, 6, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{8, 10, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{8, 14, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{9, 7, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{9, 10, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{9, 15, Corner::Edges::TOP, Edge::Corners::LEFT},

	{10, 8, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{10, 11, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{10, 16, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{11, 11, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{11, 17, Corner::Edges::TOP, Edge::Corners::LEFT},

	{12, 12, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{12, 20, Corner::Edges::TOP, Edge::Corners::LEFT},

	{13, 13, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{13, 18, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{13, 21, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{14, 14, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{14, 18, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{14, 22, Corner::Edges::TOP, Edge::Corners::LEFT},

	{15, 15, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{15, 19, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{15, 23, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{16, 16, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{16, 19, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{16, 24, Corner::Edges::TOP, Edge::Corners::LEFT},

	{17, 17, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{17, 25, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{18, 20, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{18, 26, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{18, 29, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{19, 21, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{19, 26, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{19, 30, Corner::Edges::TOP, Edge::Corners::LEFT},

	{20, 22, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{20, 27, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{20, 31, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{21, 23, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{21, 27, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{21, 32, Corner::Edges::TOP, Edge::Corners::LEFT},

	{22, 24, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{22, 28, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{22, 41, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{23, 25, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{23, 28, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{23, 34, Corner::Edges::TOP, Edge::Corners::LEFT},

	{24, 29, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{24, 37, Corner::Edges::TOP, Edge::Corners::LEFT},

	{25, 30, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{25, 35, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{25, 38, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{26, 31, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{26, 35, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{26, 39, Corner::Edges::TOP, Edge::Corners::LEFT},

	{27, 32, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{27, 36, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{27, 40, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{28, 33, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{28, 36, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{28, 41, Corner::Edges::TOP, Edge::Corners::LEFT},

	{29, 34, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{29, 42, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{30, 37, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{30, 43, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{30, 46, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{31, 38, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{31, 43, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{31, 47, Corner::Edges::TOP, Edge::Corners::LEFT},

	{32, 39, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{32, 44, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{32, 48, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{33, 40, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{33, 44, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{33, 49, Corner::Edges::TOP, Edge::Corners::LEFT},

	{34, 41, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{34, 45, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{34, 50, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{35, 42, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{35, 45, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{35, 51, Corner::Edges::TOP, Edge::Corners::LEFT},

	{36, 46, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{36, 47, Corner::Edges::TOP, Edge::Corners::LEFT},

	{37, 47, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{37, 52, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{37, 55, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{38, 48, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{38, 52, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{38, 56, Corner::Edges::TOP, Edge::Corners::LEFT},

	{39, 49, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{39, 53, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{39, 57, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{40, 50, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{40, 53, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{40, 58, Corner::Edges::TOP, Edge::Corners::LEFT},

	{41, 51, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{41, 59, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{42, 54, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{42, 60, Corner::Edges::SIDE, Edge::Corners::LEFT},

	{43, 55, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{43, 60, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{43, 63, Corner::Edges::TOP, Edge::Corners::LEFT},

	{44, 56, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{44, 61, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{44, 64, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{45, 57, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{45, 61, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{45, 65, Corner::Edges::TOP, Edge::Corners::LEFT},

	{46, 58, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{46, 62, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{46, 66, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{47, 59, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{47, 62, Corner::Edges::SIDE, Edge::Corners::RIGHT},

	{48, 63, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{48, 67, Corner::Edges::SIDE, Edge::Corners::LEFT},

	{49, 64, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{49, 67, Corner::Edges::SIDE, Edge::Corners::RIGHT},
	{49, 69, Corner::Edges::TOP, Edge::Corners::LEFT},

	{50, 65, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{50, 68, Corner::Edges::SIDE, Edge::Corners::LEFT},
	{50, 70, Corner::Edges::TOP, Edge::Corners::RIGHT},

	{51, 66, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{51, 68, Corner::Edges::SIDE, Edge::Corners::RIGHT},

	{52, 69, Corner::Edges::BOTTOM, Edge::Corners::RIGHT},
	{52, 71, Corner::Edges::SIDE, Edge::Corners::LEFT},

	{53, 70, Corner::Edges::BOTTOM, Edge::Corners::LEFT},
	{53, 71, Corner::Edges::SIDE, Edge::Corners::RIGHT}
};


void associate_terrain()
{
	for(uint16_t x = 0; x < sizeof(HEXAGON_CORNERS)/sizeof(uint8_t[4]); x++)
	{
		uint16_t hexagon_index = HEXAGON_CORNERS[x][0];
		uint16_t corner_index = HEXAGON_CORNERS[x][1];
		uint16_t hexagons_corner = HEXAGON_CORNERS[x][2];
		uint16_t corners_hexagon = HEXAGON_CORNERS[x][3];
		HEXAGONS[hexagon_index].corner(hexagons_corner, CORNERS[corner_index]);
		CORNERS[corner_index].hexagon(corners_hexagon, HEXAGONS[hexagon_index]);
	}

	for(uint16_t x = 0; x < sizeof(HEXAGON_EDGES)/sizeof(uint8_t[4]); x++)
	{
		uint16_t hexagon_index = HEXAGON_EDGES[x][0];
		uint16_t edge_index = HEXAGON_EDGES[x][1];
		uint16_t hexagons_edge = HEXAGON_EDGES[x][2];
		uint16_t edges_hexagon = HEXAGON_EDGES[x][3];
		HEXAGONS[hexagon_index].edge(hexagons_edge, EDGES[edge_index]);
		EDGES[edge_index].hexagon(edges_hexagon, HEXAGONS[hexagon_index]);
	}

	for(uint16_t x = 0; x < sizeof(CORNER_EDGES)/sizeof(uint8_t[4]); x++)
	{
		uint16_t corner_index = CORNER_EDGES[x][0];
		uint16_t edge_index = CORNER_EDGES[x][1];
		uint16_t corners_edge = CORNER_EDGES[x][2];
		uint16_t edges_corner = HEXAGON_EDGES[x][3];
		CORNERS[corner_index].edge(corners_edge, EDGES[edge_index]);
		EDGES[edge_index].corner(edges_corner, CORNERS[corner_index]);
	}
}
