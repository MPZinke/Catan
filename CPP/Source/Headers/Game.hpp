

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

		Corner* corner(uint16_t id);  // TODO: Move to private
		Edge* edge(uint16_t id);  // TODO: Move to private
		Hexagon* hexagon(uint16_t id);  // TODO: Move to private

		bool add_Player_village_to_corner(uint16_t player_id, uint16_t corner_id);
		void roll_dice();
		bool upgrade_Player_village_to_city(uint16_t player_id, uint16_t settlement_id);

	private:
		void associate_parts(json& game_data);
		void associate_corner_with_parts(json& game_data);
		void associate_edge_with_parts(json& game_data);
		void associate_hexagon_with_parts(json& game_data);

		bool distribute_resources();
		std::vector<Player*> move_robber();

		Player* player(uint16_t id);
		Player* settlement(uint16_t id);

		std::vector<Corner*> _corners;
		std::vector<Edge*> _edges;
		std::vector<Hexagon*> _hexagons;
		std::vector<Port*> _ports;

		Player* current_player = nullptr;
		std::vector<Player*> _players;
		std::vector<Settlement*> _settlements;

		DiceRoll _roll;
		uint16_t _resource_counts[RESOURCETYPE_LENGTH];

		Robber* _robber;
};
