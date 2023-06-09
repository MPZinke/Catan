

#include <nlohmann/json.hpp>


#include "Corner.hpp"
#include "DiceRoll.hpp"
#include "Edge.hpp"
#include "Hexagon.hpp"
#include "Player.hpp"
#include "Port.hpp"
#include "ResourceType.hpp"
#include "Settlement.hpp"


class Game
{
	public:
		Game(std::string filename);

		Corner* corner(uint16_t id);
		Edge* edge(uint16_t id);
		Hexagon* hexagon(uint16_t id);

		void roll_dice();

	private:
		void associate_parts(json& game_data);
		void associate_corner_with_parts(json& game_data);
		void associate_edge_with_parts(json& game_data);
		void associate_hexagon_with_parts(json& game_data);

		std::vector<Corner*> _corners;
		std::vector<Edge*> _edges;
		std::vector<Hexagon*> _hexagons;
		std::vector<Port*> _ports;

		std::vector<Player*> _players;
		std::vector<Settlement*> _settlements;

		DiceRoll _roll;
		uint16_t _resource_counts[RESOURCETYPE_LENGTH] = {0, 30, 30, 30, 30, 30};

		Robber* _robber;
};
