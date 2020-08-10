form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    postFormData("/catcher", new FormData(form_sheet))
    .then(response =>{
        console.log(response["place"]["lat"])+console.log(response["place"]["lng"]);
         othermap = new google.maps.Map(document.getElementById("place"),
                    {
                        center: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
                        zoom: response["place"]["zoom"]
                    });
                    marker = new google.maps.Marker(
                    {
                        position: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
                        map: othermap
                    })
    })
})