form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    postFormData("/catcher", new FormData(form_sheet))
<<<<<<< HEAD
    .then(response => {console.log(response);document.querySelector("#response").textContent=response["article"];})
=======
    .then(response => {document.querySelector("#response").textContent=response["article"];})
>>>>>>> 1.4_dev
})

