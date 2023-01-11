

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
				RIGHT
			};
		};

		struct Hexagons
		{
			enum
			{
				BOTTOM,
				TOP
			};
		};

		Edge(uint16_t id);

	private:
		const uint16_t _id;

		Corner* _corners[2] = {nullptr, nullptr};
		Hexagon* _hexagons[2] = {nullptr, nullptr};
};
