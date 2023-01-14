

#pragma once


#include <stdint.h>


class Corner;
class Hexagon;


class Edge
{
	public:
		struct Corners
		{
			enum
			{
				LEFT,
				RIGHT,
				CORNERS_LENGTH
			};
		};

		struct Hexagons
		{
			enum
			{
				BOTTOM,
				TOP,
				HEXAGONS_LENGTH
			};
		};

		Edge(uint16_t id);

		// ———— GETTERS ———— //
		Corner* corner(uint16_t corner);
		Hexagon* hexagon(uint16_t hexagon);
		Hexagon* operator^(Hexagon* hexagon);

		// ———— SETTERS ———— //
		void corner(uint16_t corner, Corner& new_corner);
		void corner(uint16_t corner, Corner* new_corner);

		void hexagon(uint16_t hexagon, Hexagon& new_hexagon);
		void hexagon(uint16_t hexagon, Hexagon* new_hexagon);


	private:
		const uint16_t _id;

		Corner* _corners[2] = {nullptr, nullptr};
		Hexagon* _hexagons[2] = {nullptr, nullptr};
};
