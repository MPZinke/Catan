

#include <stdint.h>


#include "ResourceType.hpp"


class Resources
{
	public:
		Resources();

		uint16_t get(ResourceType resource_type, uint16_t amount);
		void replace(ResourceType resource_type, uint16_t amount);

	private:
		uint16_t _resource_counts[6] = {30, 30, 30, 30, 30, 30};
};
