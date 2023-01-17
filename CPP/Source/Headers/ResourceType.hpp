

#pragma once


#include <nlohmann/json.hpp>
#include <string>


#include "Association.hpp"


using namespace nlohmann;


typedef uint16_t Resource;


enum ResourceType
{
	DESERT,
	WOOD,
	STONE,
	BRICK,
	WHEAT,
	SHEEP,
	RESOURCETYPE_LENGTH
};


ResourceType resource_type_for_label(std::string name);
