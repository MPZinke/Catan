export function get_lobby_status() {
    const lobby_uuid = window.location.pathname.split('/')[2];
    const url = `/api/lobby/${lobby_uuid}`;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", url, false);
    xmlhttp.send();
    if (xmlhttp.status == 400) {
        alert("There was an error 400");
        throw new Error("There was an error 400");
    }
    else if (xmlhttp.status != 200) {
        alert("get_board_data::something else other than 200 was returned");
        throw new Error("get_board_data::something else other than 200 was returned");
    }
    return JSON.parse(xmlhttp.responseText);
}
export function get_lobby_status_html() {
    const lobby_uuid = window.location.pathname.split('/')[2];
    const url = `/lobby/${lobby_uuid}/html`;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", url, false);
    xmlhttp.send();
    if (xmlhttp.status == 400) {
        alert("There was an error 400");
        throw new Error("There was an error 400");
    }
    else if (xmlhttp.status != 200) {
        alert("get_board_data::something else other than 200 was returned");
        throw new Error("get_board_data::something else other than 200 was returned");
    }
    return xmlhttp.responseText;
}
export function update_player_color(color_id) {
    const lobby_uuid = window.location.pathname.split('/')[2];
    const url = `/api/lobby/${lobby_uuid}/player/color`;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", url, false);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.send(`{"id": ${color_id}}`);
    if (xmlhttp.status == 400) {
        alert("There was an error 400");
        throw new Error("There was an error 400");
    }
    else if (xmlhttp.status != 200) {
        alert("update_player_color::something else other than 200 was returned");
        throw new Error("update_player_color::something else other than 200 was returned");
    }
    return JSON.parse(xmlhttp.responseText).success;
}
