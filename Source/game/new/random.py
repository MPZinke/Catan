

from typing import Any, Dict
from random import randint


from board import BoardTemplateData
from database import queries as db


BoardPartID = int
DictList = list[dict]
ResourceTypeID = int


class ResourceAndValueMapping:
	def __init__(self, port_resources_dict: Dict[BoardPartID, ResourceTypeID],
		tile_dice_values_dict: Dict[BoardPartID, int], tile_resources_dict: Dict[BoardPartID, ResourceTypeID]
	):
		self.port_resources_dict: Dict[BoardPartID, ResourceTypeID] = port_resources_dict
		self.tile_dice_values_dict: Dict[BoardPartID, int] = tile_dice_values_dict
		self.tile_resources_dict: Dict[BoardPartID, ResourceTypeID] = tile_resources_dict


def random_key_from_dictionary_for_available_items(dictionary: Dict[Any, int]) -> int:
	keys = list(dictionary.keys())
	key_index = randint(0, len(keys)-1)  # FROM: https://docs.python.org/3/library/random.html#random.randint
	for increment in range(0, len(keys)):
		key = keys[(key_index + increment) % len(keys)]
		if(dictionary[key] != 0):
			dictionary[key] -= 1
			return key

	raise IndexError("There are not available items in the provided dictionary.")


def resources_and_values(board_data: BoardTemplateData) -> ResourceAndValueMapping:
	port_random_resources_dict: Dict[BoardPartID, ResourceTypeID] = port_dicts_resources(board_data.id, board_data.ports)
	tile_random_dice_values_dict: Dict[BoardPartID, int] = tile_dicts_dice_values(board_data.id,board_data.tiles)
	tile_random_resources_dict: Dict[BoardPartID, ResourceTypeID] = tile_dicts_resources(board_data.id, board_data.tiles)

	return ResourceAndValueMapping(port_random_resources_dict, tile_random_dice_values_dict,
		tile_random_resources_dict
	)


def port_dicts_resources(board_id: int, port_dicts: DictList) -> Dict[BoardPartID, ResourceTypeID]:
	ports_resource_types_counts_list: DictList = db.counts.get_ports_resource_types_counts(board_id)  # pylint: disable=no-value-for-parameter
	ports_resource_types_counts = {dictionary["ResourceTypes.id"]: dictionary["count"]
		for dictionary in ports_resource_types_counts_list
	}

	port_id_resource_type_id_mappings: Dict[BoardPartID, ResourceTypeID] = {}
	for port_dict in port_dicts:
		board_port_id: BoardPartID = port_dict["id"]
		resource_type_id: ResourceTypeID = random_key_from_dictionary_for_available_items(ports_resource_types_counts)
		port_id_resource_type_id_mappings[board_port_id] = resource_type_id

	return port_id_resource_type_id_mappings


def tile_dicts_dice_values(board_id: int, tile_dicts: DictList) -> Dict[BoardPartID, ResourceTypeID]:
	dice_value_counts_list: DictList = db.counts.get_dice_value_counts(board_id)  # pylint: disable=no-value-for-parameter
	dice_value_counts = {dictionary["value"]: dictionary["count"] for dictionary in dice_value_counts_list}

	tile_id_value_mappings: Dict[BoardPartID, int] = {}
	for tile_dict in tile_dicts:
		board_tile_id: BoardPartID = tile_dict["id"]
		value = random_key_from_dictionary_for_available_items(dice_value_counts)

		tile_id_value_mappings[board_tile_id] = value

	return tile_id_value_mappings


def tile_dicts_resources(board_id: int, tile_dicts: DictList) -> Dict[BoardPartID, ResourceTypeID]:
	tiles_resource_types_counts_list: DictList = db.counts.get_tiles_resource_types_counts(board_id)  # pylint: disable=no-value-for-parameter
	tiles_resource_types_counts = {dictionary["ResourceTypes.id"]: dictionary["count"]
		for dictionary in tiles_resource_types_counts_list
	}

	tile_id_resource_type_id_mappings: Dict[BoardPartID, ResourceTypeID] = {}
	for tile_dict in tile_dicts:
		board_tile_id: BoardPartID = tile_dict["id"]
		resource_type_id: ResourceTypeID = random_key_from_dictionary_for_available_items(tiles_resource_types_counts)
		tile_id_resource_type_id_mappings[board_tile_id] = resource_type_id

	return tile_id_resource_type_id_mappings
