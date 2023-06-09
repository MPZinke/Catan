

#include "Player.hpp"


Settlement* Player::settlement(Corner* corner)
{
	for(uint8_t x = 0; x < 9; x++)
	{
		return nullptr;
	}
	return nullptr;
}


bool Player::decrement_resource(Resource type, uint16_t amount)
{
	if(type >= ResourceType::RESOURCETYPE_LENGTH)
	{
		std::exit(1);
	}

	if(_resource_counts[type] < amount)
	{
		return false;
	}

	_resource_counts[type] -= amount;
	return true;
}


void Player::increment_resource(Resource type, uint16_t amount)
{
	if(type >= ResourceType::RESOURCETYPE_LENGTH)
	{
		std::exit(1);
	}

	_resource_counts[type] += amount;
}
