let form_sheet = document.querySelector("#form-area");
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
    postFormData("/catcher", new FormData(form_sheet))
    .then(response =>{console.log(response);})
})
