

import { DirectionsAssociations } from "../Types.d.js";


export function get_directions(): DirectionsAssociations
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/directions", false);
	xmlhttp.send();
	if(xmlhttp.status == 400)
	{
		alert("There was an error 400");
		throw new Error("There was an error 400");
	}
	else if(xmlhttp.status != 200)
	{
		alert("get_directions::something else other than 200 was returned");
		throw new Error("get_directions::something else other than 200 was returned");
	}

	return JSON.parse(xmlhttp.responseText) as DirectionsAssociations;
}
