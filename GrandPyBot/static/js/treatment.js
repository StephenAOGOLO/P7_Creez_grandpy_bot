let form_sheet = document.querySelector("#form-area");
form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    console.log("Votre texte a bien été envoyé !!!");
    fetch("/sender",
    {
        method: "POST",
        body: new FormData(form)
    });
})
