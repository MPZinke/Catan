

import { Constants } from "./Types.d.js";
import { get_constants } from "./Requests/index.js";
// import { get_directions, get_player_colors, get_resource_types } from "./Requests/index.js";


export const {DIRECTIONS, PLAYER_COLORS, RESOURCE_TYPES} = get_constants() as Constants;
// export const DIRECTIONS = get_directions();
// export const PLAYER_COLORS = get_player_colors()
// export const RESOURCE_TYPES = get_resource_types();
