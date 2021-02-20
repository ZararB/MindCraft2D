
function expandNode(sender) {

    var nodeId = sender.id ;

    console.log(nodeId);


    //TODO: Open window showing details of node

}

function addNode(sender) {

    var nodeId = sender.id ;

    // TODO: Draw add node menu 




}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteNode(sender) { 

    var nodeId = sender.id ;
    var rootNodeLabel = document.getElementsByClassName('rootNode')[0].id;

    const url = "http://127.0.0.1:8000/deleteNode";

    const data = {
        "nodeId" : nodeId,
        "rootNodeLabel" : rootNodeLabel
    }

    csrftoken = getCookie('csrftoken');

    var graph ; 

    let promise = fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFTOKEN': csrftoken
        },
        body: JSON.stringify(data)
    }).then(res => res.json()).then(data => window.location.reload(true)).catch(err => console.log(err));
    
    

}

function drawGraph(graph) {

    //TODO Draw the nodes and edges at their respect positions



}

function move() {

    //TODO Move graph depending on user input like wasd and/or mosue drags
}


