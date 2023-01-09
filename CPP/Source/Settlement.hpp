

class Corner;
class Player;


class Settlement
{
	enum Type
	{
		VILLAGE,
		CITY
	};

	private:
		uint16_t _id;
		Type _type = Settlement::VILLAGE;

		Player* _player = nullptr;
		Corner* _corner = nullptr;
};


class Village: Settlement
{
	private:
		Type _type = Settlement::VILLAGE;

	public:
		Village();
};


class City: Settlement
{
	private:
		Type _type = Settlement::CITY;

	public:
		City();
};
