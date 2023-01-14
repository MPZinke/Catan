

#pragma once


#include <stdint.h>


class Player
{
	public:
		Player(uint16_t id);	

	private:
		uint16_t _id;

		Resource _resource_counts[RESOURCETYPE_LENGTH] = {0, 0, 0, 0, 0, 0};
		Settlement* _towns[5] = {nullptr, nullptr, nullptr, nullptr, nullptr};
		Settlement* _cities[4] = {nullptr, nullptr, nullptr, nullptr};
		Edge* _roads[15] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr,
		  nullptr, nullptr, nullptr, nullptr, nullptr};
};
