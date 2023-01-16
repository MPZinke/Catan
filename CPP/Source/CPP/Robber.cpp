

#include "Robber.hpp"


Robber::Robber(Hexagon* _starting_hexagon)
: _hexagon{starting_hexagon}
{

}

Hexagon* Robber::hexagon()
{
	return _hexagon;
}
