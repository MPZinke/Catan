

/*
   TWO ONE SIX
      \ | /
        ⬢
      / | \
 THREE FIVE FOUR
*/
enum CornerType
{
	ONE,
	TWO,
	THREE,
	FOUR,
	FIVE,
	SIX
}


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
}



enum HexagonType
{
	DESERT,
	WOOD,
	STONE,
	BRICK,
	WHEAT,
	SHEEP
};


class Side
{
	private:
		SideType _type
}


class Hexagon
{
	private:
		int _id;
		HexagonType _type;

}

