

#include "Port.hpp"


Port::Port(json& port_data)
: _id{port_data["id"]},
  _type{resource_type_for_label(port_data["type"])}
{}
