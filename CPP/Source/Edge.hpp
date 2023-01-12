

#pragma once


#include <stdint.h>


class Corner;
class Hexagon;


class Edge
{
	public:
		struct Corners
		{
			enum Corner
			{
				LEFT,
				RIGHT,
				CORNERS_LENGTH
			};
		};

		struct Hexagons
		{
			enum Hexagon
			{
				BOTTOM,
				TOP,
				HEXAGONS_LENGTH
			};
		};

		Edge(uint16_t id);

		// ———— GETTERS ———— //
		Corner& corner(Corners::Corner corner);
		Hexagon& hexagon(Hexagons::Hexagon hexagon);

		// ———— SETTERS ———— //
		void corner(Corners::Corner corner, Corner& new_corner);
		void hexagon(Hexagons::Hexagon hexagon, Hexagon& new_hexagon);

	private:
		const uint16_t _id;

		Corner* _corners[2] = {nullptr, nullptr};
		Hexagon* _hexagons[2] = {nullptr, nullptr};
};
