

#include <stdint.h>


/*
   TWO ONE SIX
      \ | /
        ⬢
      / | \
 THREE FIVE FOUR
*/
// enum CornerType
// {
// 	ONE,
// 	TWO,
// 	THREE,
// 	FOUR,
// 	FIVE,
// 	SIX
// };


/*
    ONE    SIX
       \ /
  TWO — ⬢ — FIVE
       / \
  THREE    FOUR
*/
enum SideType
{
	ONE,
	TWO,
	THREE,
	FOUR,
	FIVE,
	SIX
};


class Corner;
class Edge;


class Side
{
	private:
		SideType _type;
};


// namespace Hexagon
// {
// 	namespace Corners
// 	{
// 	}

// 	namespace Edges
// 	{
// 	}


// }

class Hexagon
{
	public:
		enum HexagonType
		{
			DESERT,
			WOOD,
			STONE,
			BRICK,
			WHEAT,
			SHEEP
		};

		// FROM: https://stackoverflow.com/a/15951220
		//  AND: https://en.cppreference.com/w/cpp/language/nested_types
		struct Corners
		{
			enum
			{
				BOTTOM_LEFT,
				BOTTOM_RIGHT,
				RIGHT,
				TOP_RIGHT,
				TOP_LEFT,
				LEFT
			};
		};

		struct Edges
		{
			enum
			{
				BOTTOM,
				BOTTOM_RIGHT,
				TOP_RIGHT,
				TOP,
				TOP_LEFT,
				BOTTOM_LEFT
			};
		};

	private:
		uint16_t _id;
		HexagonType _type;
		uint8_t _value;

		Corner* _corners[6] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};  // Refer to top level class
		Edge* _edges[6] = {nullptr, nullptr, nullptr, nullptr, nullptr, nullptr};  // Refer to top level class
};
