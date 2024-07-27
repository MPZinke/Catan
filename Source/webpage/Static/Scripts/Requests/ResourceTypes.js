export function get_resource_types() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/api/resource_types", false);
    xmlhttp.send();
    if (xmlhttp.status == 400) {
        alert("There was an error 400");
        throw new Error("There was an error 400");
    }
    else if (xmlhttp.status != 200) {
        alert("get_resource_types::something else other than 200 was returned");
        throw new Error("get_resource_types::something else other than 200 was returned");
    }
    return JSON.parse(xmlhttp.responseText);
}
