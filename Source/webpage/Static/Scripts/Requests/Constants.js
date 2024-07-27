export function get_constants() {
    const lobby_uuid = window.location.pathname.split('/')[2];
    const url = `/api/constants`;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", url, false);
    xmlhttp.send();
    if (xmlhttp.status == 400) {
        alert("There was an error 400");
        throw new Error("There was an error 400");
    }
    else if (xmlhttp.status != 200) {
        alert("get_constants::something else other than 200 was returned");
        throw new Error("get_constants::something else other than 200 was returned");
    }
    const { directions, player_colors, resource_types } = JSON.parse(xmlhttp.responseText);
    const [DIRECTIONS, PLAYER_COLORS, RESOURCE_TYPES] = [directions, player_colors, resource_types];
    return { DIRECTIONS, PLAYER_COLORS, RESOURCE_TYPES };
}
