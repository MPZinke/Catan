import { get_lobby_status, update_player_color } from "./Requests/index.js";
function html_to_element(html) {
    return document.createRange().createContextualFragment(html);
}
document.getElementById("player_color-select").onchange =
    function change_color() {
        const player_color_select = document.getElementById("player_color-select");
        const color_id = player_color_select.value;
        if (update_player_color(color_id)) {
            window.location.reload();
        }
    };
function update_lobby_status(players) {
}
function update_lobby() {
    const lobby_status_div = document.getElementById("lobby_status-div");
    const new_lobby_status = get_lobby_status();
    console.log(new_lobby_status);
}
setInterval(() => {
    update_lobby();
}, 2000);
