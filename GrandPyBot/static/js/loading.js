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
    }
    function startLoading()
    {
        //document.querySelector(".loader-container").style.height = '120%';
        document.querySelector(".loader-container").style.height = '90%';
        document.querySelector(".loader-container").style.width = '100%';
        document.querySelector(".loader-container").style.top = '30%';
    }
    function justWait()
    {
        console.log("wait");
    }
form_sheet.addEventListener("submit", function(event)
{
    event.preventDefault();
    startLoading();
    showContent();

})

