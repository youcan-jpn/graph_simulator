//
// Calculator
//
function plotscat() {
    // Buid query parameter
    var param = {};
    param["scat-color1"] = document.getElementById("scat-color1").value;
    param["scat-color2"] = document.getElementById("scat-color2").value;
    param["scat-color3"] = document.getElementById("scat-color3").value;
    param["scat-num"] = document.getElementById("scat-num").value;
    var query = jQuery.param(param);

    // Query with a new parameter 
    $.get("/plot/scat" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//
document.getElementById("scat-plot").addEventListener("click", function(){
    plotscat();
}, false);
plotscat();
