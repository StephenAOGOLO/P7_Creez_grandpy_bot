form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    postFormData("/catcher", new FormData(form_sheet))
    .then(response =>{
        console.log(response["place"]["lat"])+console.log(response["place"]["lng"]);
         othermap = new google.maps.Map(document.getElementById("place"),
                    {
                        center: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
                        //center: {lat: 16.25 , lng: -61.58333333},
                        //center: {lat: 35.864 , lng: -90.9428},
                        zoom: response["place"]["zoom"]
                        //zoom: 4
                    });
                    marker = new google.maps.Marker(
                    {
                        position: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
                        //position: {lat: 16.25 , lng: -61.58333333},
                        //position: {lat: 35.864 , lng: -90.9428},
                        map: othermap
                    })
    })
})