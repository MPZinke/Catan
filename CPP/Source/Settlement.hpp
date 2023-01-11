

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

		void corner(Corner* corner);
		Corner* corner();

		void player(Player* player);
		Player* player();

	protected:
		uint16_t _id;
		const Type _type = Settlement::VILLAGE;

		Player* _player = nullptr;
		Corner* _corner = nullptr;
};


class Village: Settlement
{
	private:
		const Type _type = Settlement::VILLAGE;

	public:
		Village(uint16_t id);
};


class City: Settlement
{
	private:
		const Type _type = Settlement::CITY;

	public:
		City(uint16_t id);
};
