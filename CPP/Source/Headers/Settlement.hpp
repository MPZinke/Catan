

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

		bool is_blocked();

	private:
		uint16_t _id;
		const Type _type = Settlement::VILLAGE;

		const Player& _player;
		const Corner& _corner;
};
