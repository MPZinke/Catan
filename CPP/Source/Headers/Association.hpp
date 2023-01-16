

#pragma once


#include <stdint.h>
#include <string>


struct Association
{
	uint8_t _type;
	std::string _name;
};


uint8_t type_for_name(std::string name, Association associations[], uint16_t length);
