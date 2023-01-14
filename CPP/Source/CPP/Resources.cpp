

#include "Resources.hpp"


#include <iostream>


uint16_t Resources::get(ResourceType resource_type, uint16_t amount)
{
	if(resource_type >= RESOURCETYPE_LENGTH)
	{
		exit(1);
	}

	if(_resource_counts[resource_type] < amount)
	{
		uint16_t available_amount = _resource_counts[resource_type];
		_resource_counts[resource_type] = 0;
		return available_amount;
	}

	_resource_counts[resource_type] -= amount;
	return amount;
}


void Resources::replace(ResourceType resource_type, uint16_t amount)
{
	if(resource_type >= RESOURCETYPE_LENGTH)
	{
		exit(1);
	}

	_resource_counts[resource_type] += amount;
}
