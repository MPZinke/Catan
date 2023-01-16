

#pragma once


#include <stdint.h>


#include "Corner.hpp"
#include "Edge.hpp"
#include "Hexagon.hpp"
#include "ResourceType.hpp"


extern Hexagon HEXAGONS[];
extern Corner CORNERS[];
extern Edge EDGES[];
extern uint8_t HEXAGON_CORNERS[][4];
extern uint8_t HEXAGON_EDGES[][4];
extern uint8_t CORNER_EDGES[][4];


void associate_terrain();
