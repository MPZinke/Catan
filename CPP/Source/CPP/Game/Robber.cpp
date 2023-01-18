

#include "Robber.hpp"


Robber::Robber()
: _hexagon{nullptr}
{}


Robber::Robber(Hexagon* starting_hexagon)
: _hexagon{starting_hexagon}
{}


// ———————————————————————————————————————————————————— GETTERS  ———————————————————————————————————————————————————— //

Hexagon* Robber::hexagon()
{
	return _hexagon;
}


// ———————————————————————————————————————————————————— SETTERS  ———————————————————————————————————————————————————— //

void Robber::hexagon(Hexagon* hexagon)
{
	_hexagon = hexagon;
}
