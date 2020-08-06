"use strict";
let map;
function initMap()
{
    map = new google.maps.Map(document.getElementById("gmap"),
    {
        center:
        {
            //lat: 16.25,
            //lng: -61.58333333,
            lat: response["place"]["lat"]
            lng: response["place"]["lng"],
        },
        zoom: 9
    });
}
