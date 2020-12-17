//
// Calculator
//
function plotline() {
// Build query parameter
    var param = {};
    param["line-color1"] = document.getElementById("line-color1").value;
    param["line-color2"] = document.getElementById("line-color2").value;
    param["line-color3"] = document.getElementById("line-color3").value;
    param["line-num"] = document.getElementById("line-num").value;
    param["curve1"] = document.getElementById("curve1").value;
    param["curve2"] = document.getElementById("curve2").value;
    param["curve3"] = document.getElementById("curve3").value;
    var query = jQuery.param(param);

// Query with a new parameter 
    $.get("/plot/line" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//
document.getElementById("line-plot").addEventListener("click", function(){
    plotline();
}, false);
