// Following functions handle the loading icon behavior during searching phases.
    //This function hiding the website content.
    function maskContent()
    {
        document.querySelector(".loader-container").style.opacity = 0;
        setTimeout(stopLoading, 1000);
    }
    //This function showing the website content.
    function showContent()
    {
        startLoading;
        document.querySelector(".loader-container").style.opacity = 1;setTimeout(maskContent, 4000);
    }
    //This function makes the loading icon disappear.
    function stopLoading()
    {
        document.querySelector(".loader-container").style.height = '0%';
        document.querySelector(".loader-container").style.width = '0%';
        document.querySelector(".loader-container").style.top = '100%';
    }
    //This function makes the loading icon appear.
    function startLoading()
    {
        document.querySelector(".loader-container").style.height = '100%';
        document.querySelector(".loader-container").style.width = '100%';
        document.querySelector(".loader-container").style.top = '30%';
    }
    //This function is a tempo.
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
