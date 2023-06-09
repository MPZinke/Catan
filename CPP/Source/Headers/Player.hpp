

#pragma once


#include <stdint.h>


#include "ResourceType.hpp"


class Corner;
class Edge;
class Settlement;


class Player
{
	public:
		Player(uint16_t id);

		Settlement* settlement(Corner* corner);

		bool decrement_resource(Resource type, uint16_t amount);
		void increment_resource(Resource type, uint16_t amount);

	private:
		uint16_t _id;

		Resource _resource_counts[RESOURCETYPE_LENGTH] = {0, 0, 0, 0, 0, 0};
		uint8_t _settlement_count = 0;
		Settlement* _settlements[9] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};

		uint8_t _road_count = 0;
		Edge* _roads[15] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr,
		  nullptr, nullptr, nullptr, nullptr, nullptr};
};
