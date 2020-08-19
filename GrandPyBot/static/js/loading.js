    function maskContent()
    {
        document.querySelector(".loader-container").style.opacity = 0;
        setTimeout(stopLoading, 1000);

    }
    function showContent()
    {
        startLoading;
        document.querySelector(".loader-container").style.opacity = 1;setTimeout(maskContent, 3000);
    }
    function stopLoading()
    {
        document.querySelector(".loader-container").style.height = '0%';
        document.querySelector(".loader-container").style.width = '0%';
        document.querySelector(".loader-container").style.top = '100%';
        //document.querySelector("#loader").style.height = '1px';
        //document.querySelector("#loader").style.width = '1px';
        //document.querySelector(".loader-container").style.display = 'none';
        //document.querySelector(".loader").style.display = 'none';
    }
    function startLoading()
    {
        document.querySelector(".loader-container").style.height = '120%';
        document.querySelector(".loader-container").style.width = '100%';
        document.querySelector(".loader-container").style.top = '14%';
        //document.querySelector("#loader").style.height = '100px';
        //document.querySelector("#loader").style.width = '100px';
        //document.querySelector(".loader-container").style.display = 'contents';
        //document.querySelector(".loader").style.display = 'block';
    }
    function justWait()
    {
        console.log("wait");
    }
form_sheet.addEventListener("submit", function(event)
{
    //startLoading();

    event.preventDefault();
    startLoading();
    //setTimeout(startLoading, 10);
    //stopLoading();
    //startLoading();
    showContent();
    //sleep(1000);
    //stopLoading();
    //setTimeout(justWait, 3000);
    //startLoading();
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

