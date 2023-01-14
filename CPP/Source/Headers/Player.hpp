

#pragma once


#include <stdint.h>


class Player
{
	private:
		uint16_t _id;
		Resource _resource_counts[RESOURCETYPE_LENGTH] = {0, 0, 0, 0, 0, 0};

	public:
		Player(uint16_t id);	
};
