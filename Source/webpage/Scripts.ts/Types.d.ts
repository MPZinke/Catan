

export interface Constants
{
	"DIRECTIONS": any,
	"PLAYER_COLORS": any,
	"RESOURCE_TYPES": any
}
export type Direction = "TOP"|"BOTTOM"|"SIDE"|"LEFT"|"RIGHT"|"TOP_LEFT"|"TOP_RIGHT"|"BOTTOM_LEFT"|"BOTTOM_RIGHT";
export type Directions = {[direction: string]: Index};
export interface DirectionsAssociations
{
	"Corner's Edges": Directions,
	"Corner's Sides": Directions,
	"Edge's Corners": Directions,
	"Edge's Sides": Directions,
	"Side's Corners": Directions,
	"Side's Edges": Directions,
}
export type Index = number;

export type ResourceCount = number;
export type ResourceType = number;
export type ResourceTypes = {[resource_type_name: string]: ResourceType};
export type ResourceCounts = {[resource_type: ResourceType]: number};
export type SettlementType = number;
