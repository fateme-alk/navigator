let init_graph_btn = document.getElementById('init_graph_btn');
init_graph_btn.addEventListener('click', plotInitialGraph);

let shortest_path_btn = document.getElementById('shortest_path_btn');
shortest_path_btn.addEventListener('click', showShortestPath);


function addMarker(coordinate) {
    L.marker(coordinate).addTo(myMap);
}


function addPath(p1_coordinate, p2_coordinate, color) {
    L.polyline([p1_coordinate, p2_coordinate], { color: color }).addTo(myMap);
}


function addPopup(coordinate, content) {
    L.popup()
        .setLatLng([coordinate[0]+0.0001, coordinate[1]])
        .setContent(content)
        .addTo(myMap);
}


function plotInitialGraph() {
    const url = 'http://127.0.0.1:5000/initial_graph'
    fetch(url)
        .then(response => response.json())
        .then(data => {
            Object.keys(data).forEach(key => {
                addMarker(data[key]['coordinate']);
                addPopup(data[key]['coordinate'], key);
                Object.keys(data[key]['neighbors']).forEach(neighbor_index => {
                    addPath(data[key]['coordinate'], data[key]['neighbors'][neighbor_index], 'blue');
                });
            });
        })
}


function showShortestPath() {
    const url = 'http://127.0.0.1:5000/shortest_path'
    fetch(url)
        .then(response => response.json())
        .then(data => {
            let first_vertex_pointer = 0;
            let second_vertex_pointer = 1;
            while (second_vertex_pointer < data.length) {
                const first_vertex = data[first_vertex_pointer];
                const second_vertex = data[second_vertex_pointer];
                addPath(first_vertex, second_vertex, 'red');
                first_vertex_pointer++;
                second_vertex_pointer++;
            }
        })
}
