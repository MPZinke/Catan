

class Enum:
	def __init_subclass__(cls):
		"""
		Produces an enum class by producing an integer value for the provided SUGAR keys/attributes.
		EG. `FIRST`, `SECOND`, & `THIRD` are all keys with values of `0`, `1`, `2` respectively
		```
			class Order(Enum):
				FIRST: int
				SECOND: int
				THIRD: int
		```
		"""
		enumerations: dict = cls.__annotations__
		enum = dict(zip(enumerations, range(len(enumerations))))
		for enum_key, enum_value in enum.items():
			setattr(cls, enum_key, enum_value)

		# Used to get the integer value for a give enum key as a string.
		setattr(cls, "ENUM_VALUES", enum)
		# Used to get the enum key as a string for a given integer value.
		setattr(cls, "ENUM_KEYS", {value: key for key, value in enum.items()})
