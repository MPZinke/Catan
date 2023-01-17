

#include <nlohmann/json.hpp>


class Port
{
	public:
		enum Type
		{
			ANY,
			WOOD=WOOD,
			STONE=STONE,
			BRICK=BRICK,
			WHEAT=WHEAT,
			SHEEP=SHEEP,
		};

		Port(uint16_t id);
		Port(json& port_data);

	private:
		const uint16_t _id;
		const Type _type;

		Corner* _corner;
};
