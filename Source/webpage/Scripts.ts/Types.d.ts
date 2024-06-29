

type ResourceCount = number;
type ResourceType = number;
type ResourceTypes = {[resource_type_name: string]: ResourceType};
type ResourceCounts = {[resource_type: ResourceType]: number};
type SettlementType = number;


export { ResourceCount, ResourceType, ResourceTypes, ResourceCounts, SettlementType };
