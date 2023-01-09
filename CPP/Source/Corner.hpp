

#include <stdint.h>


class Edge;
class Hexagon;
class Settlement;


class Corner
{
	public:
		struct Edges
		{
			enum
			{
				BOTTOM,
				TOP,
				SIDE
			};
		};

		struct Hexagons
		{
			enum
			{
				BOTTOM,
				TOP,
				SIDE
			};
		};

	private:
		uint16_t _id;
		Settlement* _settlement = nullptr;
		Port* _port = nullptr;

		Edge* _edges[3] = {nullptr, nullptr, nullptr};
		Hexagon* _hexagons[3] = {nullptr, nullptr, nullptr};
};
