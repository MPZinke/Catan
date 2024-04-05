#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.04                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


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

		# Used to get the enum key as a string for a given integer value.
		cls.ENUM_KEYS = {value: key for key, value in enum.items()}
		# Used to get the integer value for a give enum key as a string.
		cls.ENUM_VALUES = enum

		cls.length: int = len(enum)
		cls.items: callable = enum.items
		cls.keys: callable = enum.keys
		cls.values: callable = enum.values
