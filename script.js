// script.js

// Define the URL of the iframe
var srcUrl = "https://cobaltzvc-hyperbot.hf.space";

// Define a function to set the src attribute of the iframe element
function setIframeSrc() {
  document.getElementById("myIframe").src = srcUrl;
}

window.addEventListener("DOMContentLoaded", setIframeSrc);
