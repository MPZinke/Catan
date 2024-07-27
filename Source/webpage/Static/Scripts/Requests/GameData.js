export function get_game_data() {
    const game_id = window.location.pathname.split('/')[2];
    const url = `/api/game/${game_id}`;
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
