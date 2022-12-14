

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
			enum Corner
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
			enum Edge
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

		// ———— GETTERS ———— //
		Corner& corner(Corners::Corner corner);
		Edge& edge(Edges::Edge edge);

		ResourceType type();
		uint8_t value();

		// ———— SETTERS ———— //
		void corner(Corners::Corner corner, Corner& new_corner);
		void edge(Edges::Edge edge, Edge& new_edge);

	private:
		const uint16_t _id;
		const ResourceType _type;
		const uint8_t _value;

		Corner* _corners[Corners::CORNERS_LENGTH] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};
		Edge* _edges[6] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};
};
