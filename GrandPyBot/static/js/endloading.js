function showContent()
{
    document.querySelector(".loader-container").classList.add("hidden");
    //document.querySelector(".loader-container").classList.style.opacity = "0";
    document.getElementsByClassName("loader-container").style.opacity = "0";
}
setTimeout(showContent, 3000);
