//
// Calculator
//
function plothist() {
    // Buid query parameter
        var param = {};
        param["hist-color1"] = document.getElementById("hist-color1").value;
        param["hist-color2"] = document.getElementById("hist-color2").value;
        param["hist-color3"] = document.getElementById("hist-color3").value;
        param["hist-num"] = document.getElementById("hist-num").value;
        param["hist-alpha-value"] = document.getElementById("hist-alpha-value").value;
        var query = jQuery.param(param);
    
    // Query with a new parameter 
        $.get("/plot/hist" + "?" + query, function(data) {
            document.getElementById("plotimg").src = data;
        });
    };
    //
    // Register Event handler
    //
    document.getElementById("hist-plot").addEventListener("click", function(){
        plothist();
    }, false);
    plothist();
