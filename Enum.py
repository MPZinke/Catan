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


def Enum(name: str, **kwargs: dict) -> object:
	enum = kwargs.copy()

	return type(f"Enum::{name}", tuple(),
		{
			**kwargs,
			"length": len(enum),
			"items": enum.items,
			"keys": enum.keys,
			"values": enum.values,
			"ENUM_KEYS": {value: key for key, value in enum.items()},
			"ENUM_VALUES": enum
		}
	)
