from DataTools.Graph import Graph

def dijkstra_shortest_path(graph, start, target):
    distances = {node:(None, float('inf')) for node in graph.nodes.keys()}
    distances.pop(start)
    path = {start:(start, 0)}

    while distances:
        for traversed in path:
            for connection in graph.nodes[traversed].edges:
                if connection not in path.keys():
                    route = path[traversed][1] + graph.nodes[traversed].edges[connection]
                    if(route < distances[connection][1]):
                        distances[connection] = (traversed, route)
        shortest = (None, float('inf'))
        destination = None
        for node in distances:
            if (distances[node][1] < shortest[1]):
                shortest = distances[node]
                destination = node
        path[destination] = shortest


        distances.pop(destination)
    return path

graph = Graph()
graph.add('a', {'b':15, 'd':23, 'i':33})
graph.add('b', {'e':6, 'c':9})
graph.add('c', {'d':12})    
graph.add('d', {'e':46, 'g':3, 'i':2})
graph.add('e', {'f':14, 'h':4})
graph.add('i', {'j':5})

start = 'b'
target = 'g'
path = dijkstra_shortest_path(graph, start, target)
print(f"\nOverall shortest paths from {start} to each node:\n{path}\n")

path_visual = ""
active = target
while active != start:
    previous = path[active][0]
    cost = path[active][1]-path[previous][1]
    path_visual = f'{previous} -{cost}- > {path_visual}'
    active = previous
path_visual = path_visual+target
print(path_visual)
print(f"Lowest cost of {start} --  > {target} = {path[target][1]}\n")




