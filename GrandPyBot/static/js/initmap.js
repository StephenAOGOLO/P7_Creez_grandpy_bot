form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    postFormData("/catcher", new FormData(form_sheet))
    .then(response =>{
                    form = document.getElementById('form-area');
                    //var oldScript = document.getElementById('init');
                    //if (oldScript)
                    if (document.getElementById('init'))
                    {
                        form.removeChild(document.getElementById('init'));
                    }
                    var script = document.createElement('script');
                    script.src = 'https://maps.googleapis.com/maps/api/js?callback=initMap&key='+response["gmap_id"];
                    script.defer = true;
                    script.id = "init";
                    form.appendChild(script);
                        })
})