function changeView() {
    var target_value = document.getElementById('graph-type').value;
    let graphs = ['scatter','histogram'];
    for(let item of graphs) {
        if(item == target_value) {
            var display_item = document.getElementById(item);
            display_item.classList.remove('hidden');
        } else {
            var hidden_item = document.getElementById(item);
            hidden_item.classList.add('hidden');
        };
    };
};

document.getElementById("graph-type").addEventListener("input", function(){
    changeView();
}, false);
changeView();