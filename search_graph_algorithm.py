from heapq import heapify, heappop


def find_dict_key(dict, value):
            for k, v in dict.items():
                if v == value:
                    return k
                

def dijkstra(g, src, dst):
    data = {}
    for vertex in g.adj_list.keys():
        if vertex != src:
            data[vertex] = {'weight': float('inf'), 'pre':[]}
        else:
            data[vertex] = {'weight': 0, 'pre':[]}
    
    explored_vertices = set()
    curr_vertex = src
    
    while curr_vertex != dst:
        explored_vertices.add(curr_vertex)
        possible_weights = []
        adj_vertex_dict = {}
        for adj_vertex, weight in g.adj_list[curr_vertex].items():
            if adj_vertex not in explored_vertices:
                    total_weight = data[curr_vertex]['weight'] + weight
                    if total_weight < data[adj_vertex]['weight']:
                        data[adj_vertex]['weight'] = total_weight
                        data[adj_vertex]['pre'] = data[curr_vertex]['pre'] + [curr_vertex]
                    adj_vertex_dict[adj_vertex] = total_weight
                    possible_weights.append(data[adj_vertex]['weight'])

        
        heapify(possible_weights)
        min_weight = heappop(possible_weights)
        curr_vertex = find_dict_key(adj_vertex_dict, min_weight)
    return data[dst]['weight'], data[dst]['pre']
            



                    
