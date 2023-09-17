let init_graph_btn = document.getElementById('init_graph_btn');
init_graph_btn.addEventListener('click', plotInitialGraph);


function addMarker(coordinate) {
    L.marker(coordinate).addTo(myMap);
}


function addPath(p1_coordinate, p2_coordinate, color) {
    L.polyline([p1_coordinate, p2_coordinate], { color: color }).addTo(myMap);
}


function plotInitialGraph() {
    const url = 'http://127.0.0.1:5000/initial_graph'
    fetch(url)
        .then(response => response.json())
        .then(data => {
            Object.keys(data).forEach(key => {
                addMarker(data[key]['coordinate']);
                Object.keys(data[key]['neighbors']).forEach(neighbor_index => {
                    addPath(data[key]['coordinate'], data[key]['neighbors'][neighbor_index], 'blue');
                });
            });
        })
}
