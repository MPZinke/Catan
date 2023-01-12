

#pragma once


#include <stdint.h>


class Edge;
class Hexagon;
class Port;
class Settlement;


class Corner
{
	public:
		struct Edges
		{
			enum Edge
			{
				BOTTOM,
				TOP,
				SIDE,
				EDGES_LENGTH
			};
		};

		struct Hexagons
		{
			enum Hexagon
			{
				BOTTOM,
				TOP,
				SIDE,
				HEXAGONS_LENGTH
			};
		};

		Corner(uint16_t id);

		// ———— GETTERS ———— //
		Edge& edge(Edges::Edge edge);
		Hexagon& hexagon(Hexagons::Hexagon hexagon);

		// ———— SETTERS ———— //
		void edge(Edges::Edge edge, Edge& new_edge);
		void hexagon(Hexagons::Hexagon hexagon, Hexagon& new_hexagon);

	private:
		uint16_t _id;
		Settlement* _settlement = nullptr;
		Port* _port = nullptr;

		Edge* _edges[3] = {nullptr, nullptr, nullptr};
		Hexagon* _hexagons[3] = {nullptr, nullptr, nullptr};
};
