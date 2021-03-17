import logo from './logo.svg';
import './App.css';
import React from 'react'; 
import { element } from 'prop-types';

BASE_URL = "http://127.0.0.1:8000/"

function App() {


  let data = window.location.href.replace(BASE_URL, '').split('/')
  let user = data[0]
  let rootNodeLabel = data[1]
  let rootNodeRank = data[2]

  const url = "http://127.0.0.1:8000/drawGraph";
  const data = {
      "user" : user,
      "rootNodeLabel" : rootNodeLabel,
      "rootNodeRank" : rootNodeRank
    }

  csrftoken = getCookie('csrftoken');


  let promise = await fetch({
    method: 'POST',
    headers: {
        'Content-Type':'application/json',
        'X-CSRFTOKEN': csrftoken
    },
    body: JSON.stringify(data)
}).then(response => { 
      graph = response.json()
    })
    .then(graph => {
      const element = <div className="App"><p>Hello React!</p></div>;
      const graph = Graph()
      // Draw the graph

    })
    .catch(error => {
      // Handle the error 
    })
  
  return (
    element
  );

}

function Graph(props) {
  return (<div></div>)
}


function Node(props) {

  return (
    <div className="Node" id={props.id}>
      

    </div>
  )
}


function Edge(props) {
  return (<div></div>)


export default App;

function drawGraph(graph) {


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
