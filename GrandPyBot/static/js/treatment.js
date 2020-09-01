//this script handle two main features :
//  -   the AJAX behavior during the content treatments
//  -   the behavior of the content web page  during searching phases (Loading animations).
let form_sheet = document.querySelector("#form-area");
let responseArea = document.getElementById("response");
let haikuArea = document.getElementById("haiku");
let placeArea = document.getElementById("place");
//AJAX behaviour and loading animations
function req(output)
{
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		console.log(this);
		//AJAX part
		if (this.readyState == 4 && this.status == 200) {
			console.log(output);
			responseArea.innerHTML = output.article;
			responseArea.style.opacity = 1;
			//Loading animation for GrandPyBot response
			responseArea.style.transition = "opacity 3s ease-in-out, visibility 5s ease-in-out";
			//Loading animation for GrandPyBot Haiku
			haikuArea.style.transition = "opacity 3s ease-in-out, visibility 5s ease-in-out";
			//Loading animation for Google Map
			place.style.transition = "opacity 3s ease-in-out, visibility 5s ease-in-out";
			if(output.haiku == undefined)
			{
			    haikuArea.style.opacity = 0;
			}
			else
			{
			    haikuArea.innerHTML += output.haiku;
			    haikuArea.style.opacity = 1;
			}
			//Google Map initialization
			 othermap = new google.maps.Map(document.getElementById("place"),
            {
                center: { lat: output.place.lat , lng: output.place.lng},
                zoom: output.place.zoom
            });
            marker = new google.maps.Marker(
            {
                position: { lat: output.place.lat , lng: output.place.lng },
                map: othermap
            });
            place.style.opacity = 1;
		} else if (this.readyState == 4 && this.status == 404) {
			alert('Erreur 404 :/');
		}
	};
	xhr.open("GET", "/", true);
	xhr.responseType = "json";
	xhr.send();
}
function postFormData(url, data)
{
    return fetch(url,
    {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}
form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    var responseArea = document.getElementById("response");
    var placeArea = document.getElementById("place");
    //Resetting default content display
    responseArea.style.opacity = 0;
    placeArea.style.opacity = 0;
    haikuArea.style.opacity = 0;
    //GrandPyBot Response retrieval
    postFormData("/catcher", new FormData(form_sheet))
    .then(response =>{req(response);})
})
