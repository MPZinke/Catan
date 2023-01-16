

#include "Association.hpp"


#include "ResourceType.hpp"


uint8_t type_for_name(std::string name, Association associations[], uint16_t length)
{
	for(uint8_t x = 0; x < length; x++)
	{
		if(name == associations[x]._name)
		{
			return (ResourceType)associations[x]._type;
		}
	}

	std::exit(1);
}
