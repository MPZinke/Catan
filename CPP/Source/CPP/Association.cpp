

#include "Association.hpp"


#include "ResourceType.hpp"


uint8_t type_for_label(std::string label, Association associations[], uint16_t length)
{
	for(uint8_t x = 0; x < length; x++)
	{
		if(label == associations[x]._label)
		{
			return (ResourceType)associations[x]._type;
		}
	}

	std::exit(1);
}
