form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    postFormData("/catcher", new FormData(form_sheet))
    .then(response =>{
<<<<<<< HEAD
        console.log(response["place"]["lat"])+console.log(response["place"]["lng"]);
=======
        /*console.log(response["place"]["lat"])+console.log(response["place"]["lng"]);*/
>>>>>>> 1.4_dev
         othermap = new google.maps.Map(document.getElementById("place"),
                    {
                        center: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
                        zoom: response["place"]["zoom"]
                    });
                    marker = new google.maps.Marker(
                    {
                        position: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
                        map: othermap
                    });
    })
})
