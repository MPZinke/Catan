

#pragma once


#include <stdint.h>


class Corner;
class Player;


class Settlement
{
	public:
		enum Type
		{
			VILLAGE=1,
			CITY=2
		};

		Settlement(uint16_t id, Player* player, Corner* corner);

		// ———— GETTERS ———— //
		uint16_t id();
		Corner* corner();
		Player* player();
		Type type();

		// ———— GAME ———— //
		bool is_blocked();
		bool upgrade();

	private:
		uint16_t _id;
		Type _type = Settlement::VILLAGE;

		const Player* _player;
		const Corner* _corner;
};
