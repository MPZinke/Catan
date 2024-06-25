

from database import queries as db


DictList = list[dict]


class TemplateData:
	def __init__(self, id: int, name: str, ports: DictList, roads: DictList, settlements: DictList,
		tiles: DictList
	):
		self.id: int = id
		self.name: str = name
		self.ports: DictList = ports
		self.roads: DictList = roads
		self.settlements: DictList = settlements
		self.tiles: DictList = tiles


def template_data(template_id: int) -> TemplateData:
	name: str = db.templates.get_template(template_id)["name"]  # pylint: disable=no-value-for-parameter
	ports: DictList = db.templates.get_ports(template_id)  # pylint: disable=no-value-for-parameter
	roads: DictList = db.templates.get_roads(template_id)  # pylint: disable=no-value-for-parameter
	settlements: DictList = db.templates.get_settlements(template_id)  # pylint: disable=no-value-for-parameter
	tiles: DictList = db.templates.get_tiles(template_id)  # pylint: disable=no-value-for-parameter

	return TemplateData(template_id, name, ports, roads, settlements, tiles)
