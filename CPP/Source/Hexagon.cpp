
/***********************************************************************************************************************
*                                                                                                                      *
*   created by: MPZinke                                                                                                *
*   on 2023.01.09                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION: TEMPLATE                                                                                              *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


#include "Hexagon.hpp"


#include <iostream>


Hexagon::Hexagon(uint16_t id, ResourceType type, uint8_t value/*=0*/)
: _id{id}, _type{type}, _value{value}
{}


Corner* Hexagon::corner(Corners::type corner)
{
	if(corner < Corners::CORNERS_LENGTH)
	{
		std::exit(1);
	}

	return _corners[corner];
}



ResourceType Hexagon::type()
{
	return _type;
}


uint8_t Hexagon::value()
{
	return _value;
}
