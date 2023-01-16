

#include "ResourceType.hpp"


#include <iostream>


ResourceType resource_type_for_name(std::string name)
{
	Association resource_associations[] =
	{
		{DESERT, "DESERT"},
		{WOOD, "WOOD"},
		{STONE, "STONE"},
		{BRICK, "BRICK"},
		{WHEAT, "WHEAT"},
		{SHEEP, "SHEEP"}
	};

	return (ResourceType)type_for_name(name, resource_associations, RESOURCETYPE_LENGTH);
}
