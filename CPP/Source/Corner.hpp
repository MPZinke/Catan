

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
			enum
			{
				BOTTOM,
				TOP,
				SIDE,
				EDGES_LENGTH
			};
		};

		struct Hexagons
		{
			enum
			{
				BOTTOM,
				TOP,
				SIDE,
				HEXAGONS_LENGTH
			};
		};

		Corner(uint16_t id);

		// ———— GETTERS ———— //
		Edge* edge(uint16_t edge);
		Hexagon* hexagon(uint16_t hexagon);

		// ———— SETTERS ———— //
		void edge(uint16_t edge, Edge& new_edge);
		void edge(uint16_t edge, Edge* new_edge);

		void hexagon(uint16_t hexagon, Hexagon& new_hexagon);
		void hexagon(uint16_t hexagon, Hexagon* new_hexagon);

	private:
		uint16_t _id;
		Settlement* _settlement = nullptr;
		Port* _port = nullptr;

		Edge* _edges[3] = {nullptr, nullptr, nullptr};
		Hexagon* _hexagons[3] = {nullptr, nullptr, nullptr};
};
