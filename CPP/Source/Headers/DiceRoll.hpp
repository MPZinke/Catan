
/***********************************************************************************************************************
*                                                                                                                      *
*   created by: MPZinke                                                                                                *
*   on 2023.06.08                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION: TEMPLATE                                                                                              *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


#pragma once


#include <stdint.h>


class Hexagon;


class DiceRoll
{
	private:
		uint8_t _value;

	public:
		DiceRoll();

		uint8_t value();
		bool operator==(uint8_t value);
		friend bool operator==(Hexagon& value, DiceRoll& roll);
		friend bool operator==(Hexagon* value, DiceRoll& roll);
};
