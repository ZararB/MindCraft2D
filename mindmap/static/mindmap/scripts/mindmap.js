function expandNode(sender) {

    var nodeId = sender.id ;

    console.log(nodeId);


    //TODO: Open window showing details of node

}

function addNode(sender) {

    var nodeId = sender.id ;

    // TODO: Draw add node menu 




}

function deleteNode(sender) {

    //TODO Figure out how to send httpRequests and display responses 
    

    var nodeId = sender.id ;
    var rootNodeLabel = document.getElementsByClassName('rootNode')[0].id;

    const url = "http://127.0.0.1:8000/deleteNode";
    const data = {
        "nodeId" : nodeId,
        "rootNodeLabel" : rootNodeLabel
    }
    
    const response = await fetch(url, {
     
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
          },

        body: JSON.stringify(data)
    });

    

}

function drawGraph(graph) {

    //TODO Draw the nodes and edges at their respect positions

}

function move() {

    //TODO Move graph depending on user input like wasd and/or mosue drags
}