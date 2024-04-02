

class Enum:
	def __init_subclass__(cls):
		enumerations: dict = cls.__annotations__
		enum = dict(zip(enumerations, range(len(enumerations))))
		for enum_key, enum_value in enum.items():
			setattr(cls, enum_key, enum_value)

		setattr(cls, "ENUM_VALUES", enum)
		setattr(cls, "ENUM_KEYS", {value: key for key, value in enum.items()})
