

from database.queries import types
from Enum import Enum


ResourceType = Enum("ResourceType", **{type["label"]: type["id"]-1 for type in types.get_resource_types()})
