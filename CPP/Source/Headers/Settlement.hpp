

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

		Settlement(uint16_t id);

		// ———— GETTERS ———— //
		Corner* corner();
		Player* player();

		// ———— SETTERS ———— //
		void corner(Corner& corner);
		void corner(Corner* corner);
		void player(Player* player);
		void player(Player& player);

		bool is_blocked();

	private:
		uint16_t _id;
		const Type _type = Settlement::VILLAGE;

		Player* _player = nullptr;
		Corner* _corner = nullptr;
};
