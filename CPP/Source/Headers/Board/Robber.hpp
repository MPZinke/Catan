

class Hexagon;


class Robber
{
	public:
		Robber();
		Robber(Hexagon* starting_hexagon);

		// ———— GETTERS ———— //
		Hexagon* hexagon();

		// ———— SETTERS ———— //
		void hexagon(Hexagon* hexagon);

	private:
		Hexagon* _hexagon;
};
