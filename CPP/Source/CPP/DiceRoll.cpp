
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


#include "DiceRoll.hpp"


#include <stdlib.h>
#include <iostream>
#include <time.h>


DiceRoll::DiceRoll()
{
	srand(time(NULL));
	_value = rand() % 6 + 1;
	_value += rand() % 6 + 1;
}


uint8_t DiceRoll::value()
{
	return _value;
}


bool DiceRoll::operator==(uint8_t value)
{
	return _value == value;
}
