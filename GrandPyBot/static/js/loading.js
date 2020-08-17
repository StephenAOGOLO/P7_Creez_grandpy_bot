function maskContent()
{
    document.querySelector(".loader-container").style.opacity = 0;

}
function showContent()
{
    document.querySelector(".loader-container").style.opacity = 1;setTimeout(maskContent, 3000);

}
setTimeout(showContent, 3000);

