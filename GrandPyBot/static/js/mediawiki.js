form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    postFormData("/catcher", new FormData(form_sheet))
    .then(response => {console.log(response);document.querySelector("#response").textContent=response["article"];})
})

