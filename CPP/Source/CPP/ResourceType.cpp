

#include "ResourceType.hpp"


#include <iostream>


ResourceType resource_type_for_label(std::string label)
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

	return (ResourceType)type_for_label(label, resource_associations, RESOURCETYPE_LENGTH);
}
