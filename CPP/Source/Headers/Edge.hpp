

#pragma once


#include <nlohmann/json.hpp>
#include <stdint.h>


using namespace nlohmann;


class Corner;
class Hexagon;


class Edge
{
	public:
		struct Corners
		{
			/*
			Corners relative to edges
			 Edges
			  4  3  2
			   \ | / 
			     ⬣
			   / | \
			  5  0  1

			 0, 3.
			  LEFT————RIGHT

			 1, 4.
			      RIGHT
			      /
			     /
			  LEFT

			 2, 5.
			  LEFT
			   \
			    \
			    RIGHT
			*/
			enum
			{
				LEFT,
				RIGHT,
				CORNERS_LENGTH
			};
		};

		struct Hexagons
		{
			/*
			Hexagon relative to edge
			 Edges
			  4  3  2
			   \ | / 
			     ⬣
			   / | \
			  5  0  1

			 0, 3.
			   TOP
			  ——————
			  BOTTOM

			 1, 4.
			  TOP /
			     / BOTTOM

			 2, 5.
			        \ TOP
			  BOTTOM \
			*/
			enum
			{
				BOTTOM,
				TOP,
				HEXAGONS_LENGTH
			};
		};

		Edge(uint16_t id);
		Edge(json& edge_data);

		// ———— GETTERS ———— //
		// ———— GETTERS::INFO ———— //
		uint16_t id();

		// ———— GETTERS::BOARD ———— //
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
