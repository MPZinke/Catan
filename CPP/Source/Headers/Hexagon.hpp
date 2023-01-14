

#pragma once


#include <stdint.h>
#include <vector>


#include "ResourceType.hpp"


#define NUMBER_OF_HEXAGONS 19


class Corner;
class Edge;
class Robber;


class Hexagon
{
	public:
		// FROM: https://stackoverflow.com/a/15951220
		//  AND: https://en.cppreference.com/w/cpp/language/nested_types
		struct Corners
		{
			/*
			Corners relative to hexagon
			   4    3
			    \  / 
			 5 — ⬣ — 2
			    /  \
			   0    1
			*/
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
			/*
			Edges relative to hexagon
			 Edges
			  4  3  2
			   \ | / 
			     ⬣
			   / | \
			  5  0  1
			*/
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
		// ———— GETTERS::INFO ———— //
		uint16_t id();
		ResourceType type();
		uint8_t value();

		// ———— GETTERS::BOARD ———— //
		Corner* corner(uint16_t corner);
		Edge* edge(uint16_t edge);
		Hexagon* hexagon(uint16_t id);
		Robber* robber();

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
		Robber* _robber = nullptr;

		static std::vector<Hexagon*> _bfs_queue;
		static bool _visited_hexagons[NUMBER_OF_HEXAGONS];

		static bool can_be_enqueued(Hexagon* hexagon);
		static void clear_bfs_data();
		static Hexagon* pop_bfs_queue();
};
