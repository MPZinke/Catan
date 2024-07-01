

export function get_resource_types(): any
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/resource_types", false);
	xmlhttp.send();
	if(xmlhttp.status == 400)
	{
		return alert('There was an error 400');
	}
	else if(xmlhttp.status != 200)
	{
		return alert('get_resource_types::something else other than 200 was returned');
	}

	return JSON.parse(xmlhttp.responseText);
}


export function get_game_data(): any
{
	const game_id = window.location.pathname.split('/')[2];
	const url: string = `/api/game/${game_id}`;
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", url, false);
	xmlhttp.send();
	if(xmlhttp.status == 400)
	{
		return alert('There was an error 400');
	}
	else if(xmlhttp.status != 200)
	{
		return alert('get_board_data::something else other than 200 was returned');
	}

	return JSON.parse(xmlhttp.responseText);
}
