    function maskContent()
    {
        document.querySelector(".loader-container").style.opacity = 0;

    }
    function showContent()
    {
        document.querySelector(".loader-container").style.opacity = 1;setTimeout(maskContent, 3000);

    }
form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    showContent();
})


















////form_sheet.addEventListener("submit", function(event)
////{
////    event.preventDefault();
////    postFormData("/catcher", new FormData(form_sheet))
////    .then(
//    function maskContent()
//    {
//        document.querySelector(".loader-container").style.opacity = 0;
//
//    }
//    function showContent()
//    {
//        document.querySelector(".loader-container").style.opacity = 1;setTimeout(maskContent, 3000);
//
//    }
//    //setTimeout(showContent, 5000);
//    showContent();
////    )
////})

