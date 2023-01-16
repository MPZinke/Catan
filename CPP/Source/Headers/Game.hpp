

#include <nlohmann/json.hpp>


#include "Corner.hpp"
#include "Edge.hpp"
#include "Hexagon.hpp"
#include "Player.hpp"
#include "Port.hpp"
#include "ResourceType.hpp"
#include "Settlement.hpp"


class Game
{
	public:
		Game();


	private:
		std::vector<Corner*> _corners;
		std::vector<Edge*> _edges;
		std::vector<Hexagon*> _hexagons;
		std::vector<Port*> _ports;

		std::vector<Player*> _players;
		std::vector<Settlement*> _settlements;

		uint16_t _resource_counts[RESOURCETYPE_LENGTH] = {0, 30, 30, 30, 30, 30};

		Robber* _robber;
};
