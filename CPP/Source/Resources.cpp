

#include "Resources.hpp"


#include <iostream>


uint16_t Resources::get(ResourceType resource_type, uint16_t amount)
{
	if(resource_type >= RESOURCETYPE_LENGTH)
	{
		exit(1);
	}

	_resource_counts[resource_type]
}


void Resources::replace(ResourceType resource_type, uint16_t amount)
{
	if(resource_type >= RESOURCETYPE_LENGTH)
	{
		exit(1);
	}

	_resource_counts[resource_type] += amount
}
