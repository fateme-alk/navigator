from flask import Flask, after_this_request, jsonify
from search_graph_algorithm import dijkstra
import graph_instance


app = Flask(__name__)
min_distance, min_path = dijkstra(graph_instance.g1, graph_instance.e, graph_instance.b) 

@app.route('/initial_graph', methods=['GET'])
def initial_graph_route():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    

    def extract_graph_info(graph):
        graph_info = {}
        for vertex, adj_vertices in graph.adj_list.items():
            graph_info[vertex.name] = {
                 'coordinate': [vertex.lat, vertex.long],
                 'neighbors': [[adj_v.lat, adj_v.long] for adj_v in adj_vertices.keys()],
            }
        return graph_info
    
    return jsonify(extract_graph_info(graph_instance.g1))


@app.route('/shortest_path', methods=['GET'])
def shortes_path_route():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    return jsonify([[vertex.lat, vertex.long] for vertex in min_path])


if __name__ == '__main__':
    app.run()
