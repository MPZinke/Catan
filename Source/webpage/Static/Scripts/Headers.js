import { get_resource_types } from "./Requests.js";
import { HexagonGrid } from "./Layout/index.js";
import Canvas from "./Canvas.js";
export const RESOURCE_TYPES = get_resource_types();
const HEXAGON_GRID = new HexagonGrid(5, 5, 75);
const CANVAS = new Canvas(HEXAGON_GRID);
