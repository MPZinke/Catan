

#pragma once


#include <stdint.h>


#include "ResourceType.hpp"


/*
   TWO ONE SIX
      \ | /
        ⬢
      / | \
 THREE FIVE FOUR


    ONE    SIX
       \ /
  TWO — ⬢ — FIVE
       / \
  THREE    FOUR
*/


class Corner;
class Edge;


class Hexagon
{
	public:
		// FROM: https://stackoverflow.com/a/15951220
		//  AND: https://en.cppreference.com/w/cpp/language/nested_types
		struct Corners
		{
			enum type
			{
				BOTTOM_LEFT,
				BOTTOM_RIGHT,
				RIGHT,
				TOP_RIGHT,
				TOP_LEFT,
				LEFT,
				CORNERS_LENGTH
			};
		};

		struct Edges
		{
			enum type
			{
				BOTTOM,
				BOTTOM_RIGHT,
				TOP_RIGHT,
				TOP,
				TOP_LEFT,
				BOTTOM_LEFT,
				EDGES_LENGTH
			};
		};

		Hexagon(uint16_t id, ResourceType type, uint8_t value=0);

		Corner* corner(Corners::type corner);
		ResourceType type();
		uint8_t value();

	private:
		uint16_t _id;
		const ResourceType _type;
		uint8_t _value;

		Corner* _corners[Corners::CORNERS_LENGTH] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};  // Refer to top level class
		Edge* _edges[6] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};  // Refer to top level class
};
