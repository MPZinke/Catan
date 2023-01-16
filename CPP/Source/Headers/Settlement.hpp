

#pragma once


#include <stdint.h>


class Corner;
class Player;


class Settlement
{
	public:
		enum Type
		{
			VILLAGE,
			CITY
		};

		Settlement(uint16_t id, Player& player, Corner& corner);

		// ———— GETTERS ———— //
		Corner& corner();
		Player& player();

		// ———— GAME ———— //
		bool is_blocked();
		bool upgrade();

	private:
		uint16_t _id;
		Type _type = Settlement::VILLAGE;

		const Player& _player;
		const Corner& _corner;
};
