

#include <nlohmann/json.hpp>


#include "ResourceType.hpp"


class Corner;


class Port
{
	public:
		// enum ResourceType
		// {
		// 	ANY,
		// 	WOOD=WOOD,
		// 	STONE=STONE,
		// 	BRICK=BRICK,
		// 	WHEAT=WHEAT,
		// 	SHEEP=SHEEP,
		// };

		Port(uint16_t id);
		Port(json& port_data);

	private:
		const uint16_t _id;
		const ResourceType _type;

		Corner* _corner;
};
