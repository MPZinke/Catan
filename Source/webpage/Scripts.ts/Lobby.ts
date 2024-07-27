

import { get_lobby_status_html, get_lobby_status, update_player_color } from "./Requests/index.js";


function html_to_element(html: string): DocumentFragment
{
	return document.createRange().createContextualFragment(html);
}


// function update_lobby()
// {
// 	const lobby_status_div = document.getElementById("lobby_status-div") as HTMLElement;

// 	const new_lobby_status_html: string = get_lobby_status_html();
// 	const new_lobby_status_element: DocumentFragment = html_to_element(new_lobby_status_html);
// 	lobby_status_div.replaceChildren(new_lobby_status_element);
// }

document.getElementById("player_color-select")!.onchange = 
function change_color(): void
{
	const player_color_select = document.getElementById("player_color-select") as HTMLSelectElement;
	const color_id: number = player_color_select.value as any;
	if(update_player_color(color_id))
	{
		window.location.reload();
	}
}



function update_lobby_status(players: object[]): void
{

}


function update_lobby()
{
	const lobby_status_div: HTMLElement = document.getElementById("lobby_status-div") as HTMLElement;

	const new_lobby_status: object = get_lobby_status();
	// const new_lobby_status_element: DocumentFragment = html_to_element(new_lobby_status_html);
	// lobby_status_div.replaceChildren(new_lobby_status_element);
}


setInterval(
	() => {
		update_lobby();
	}, 
	2000
);
