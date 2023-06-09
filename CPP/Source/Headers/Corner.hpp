

#pragma once


#include <nlohmann/json.hpp>
#include <stdint.h>
#include <string>


using namespace nlohmann;


class Edge;
class Hexagon;
class Port;
class Settlement;


class Corner
{
	public:
		struct Edges
		{
			/*
			Edges relative to corner
			 TOP
			   \__ SIDE
			   /
			 BOTTOM

			        TOP
			 SIDE __/
			        \
			        BOTTOM
			*/
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
			/*
			Hexagons relative to corners
			          ______
			         /      \
			  ______/        \
			 /      \  TOP   /
			/  SIDE  \______/
			\        /      \
			 \______/ BOTTOM \
			        \        /
			         \______/
			  ______
			 /      \
			/        \______
			\   TOP  /      \
			 \______/  SIDE  \
			 /      \        /
			/ BOTTOM \______/
			\        /
			 \______/
			 */
			enum
			{
				BOTTOM,
				TOP,
				SIDE,
				HEXAGONS_LENGTH
			};
		};

		Corner(uint16_t id);
		Corner(json& corner_data);

		// ———— GETTERS ———— //
		// ———— GETTERS::INFO ———— //
		uint16_t id();
		uint8_t type_for_label(std::string label);

		// ———— GETTERS::BOARD ———— //
		Edge* edge(uint16_t edge);
		Hexagon* hexagon(uint16_t hexagon);
		Port* port();
		Settlement* settlement();

		// ———— SETTERS ———— //
		void edge(uint16_t edge, Edge* new_edge);
		void edge(std::string edge_label, Edge* new_edge);

		void hexagon(uint16_t hexagon, Hexagon& new_hexagon);
		void hexagon(uint16_t hexagon, Hexagon* new_hexagon);
		void hexagon(std::string hexagon_label, Hexagon* new_hexagon);

	private:
		uint16_t _id;
		Settlement* _settlement = nullptr;
		Port* _port = nullptr;

		Edge* _edges[3] = {nullptr, nullptr, nullptr};
		Hexagon* _hexagons[3] = {nullptr, nullptr, nullptr};
};
