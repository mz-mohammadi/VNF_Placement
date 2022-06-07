import queue  
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])

def dijkstra_serv(graph, source, dest, servers):  
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")
    servers_at_path=[]
    
    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)
           
    q.put(([0, source]))
      
    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]
        for e in graph.get_edge(v):
            candidate_distance = distances[int(v)] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                # primitive but effective negative cycle detection
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))


    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        if end in servers:
            servers_at_path.append(end)
        end = parents[int(end)]

    shortest_path.reverse()
    return servers_at_path

