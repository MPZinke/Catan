

#pragma once


#include <stdint.h>
#include <vector>


#include "ResourceType.hpp"


#define NUMBER_OF_HEXAGONS 19


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
			enum
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
			enum
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
		Corner* corner(uint16_t corner);
		Edge* edge(uint16_t edge);
		Hexagon* hexagon(uint16_t id);

		uint16_t id();
		ResourceType type();
		uint8_t value();

		// ———— SETTERS ———— //
		void corner(uint16_t corner, Corner& new_corner);
		void corner(uint16_t corner, Corner* new_corner);

		void edge(uint16_t edge, Edge& new_edge);
		void edge(uint16_t edge, Edge* new_edge);

	private:
		const uint16_t _id;
		const ResourceType _type;
		const uint8_t _value;

		Corner* _corners[Corners::CORNERS_LENGTH] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};
		Edge* _edges[6] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};

		static std::vector<Hexagon*> _bfs_queue;
		static bool _visited_hexagons[NUMBER_OF_HEXAGONS];

		static bool can_be_queued(Hexagon* hexagon);
		static void clear_bfs_data();
		static Hexagon* pop_bfs_queue();
};
