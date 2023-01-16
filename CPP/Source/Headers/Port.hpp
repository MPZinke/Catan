

class Port
{
	public:
		enum Type
		{
			ANY,
			WOOD=WOOD,
			STONE=STONE,
			BRICK=BRICK,
			WHEAT=WHEAT,
			SHEEP=SHEEP,
		};
		Port();

	private:
		Corner* _corner;


};
