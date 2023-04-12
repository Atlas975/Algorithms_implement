# import sys

# def bellman_ford(graph, start):
#     dist = {vertex: float('inf') for vertex in graph}
#     dist[start] = 0

#     for _ in range(len(graph) - 1):
#         for u in graph:
#             for v, weight in graph[u].items():
#                 if dist[u] + weight < dist[v]:
#                     dist[v] = dist[u] + weight

#     # Check for negative cycles
#     for u in graph:
#         for v, weight in graph[u].items():
#             if dist[u] + weight < dist[v]:
#                 sys.exit("Error: Graph contains negative weight cycle")
#     return dist


def bellman_ford(graph, origin) -> dict:  # O(VE) time, O(V) space
    distmp = {vertex: float("inf") for vertex in graph}
    distmp[origin] = 0

    # relax all edges |V| - 1 times, max number of edges in minimum spanning tree
    for _ in range(len(graph) - 1):
        for u in filter(lambda u: distmp[u] != float("inf"), graph):  # filter unreachable vertices
            for v, weight in graph[u].items():
                if (vdist := distmp[u] + weight) < distmp[v]:
                    distmp[v] = vdist

    for u in filter(lambda u: distmp[u] != float("inf"), graph):
        for v, weight in graph[u].items():  # if we can still relax, then there is a negative cycle
            if (vdist := distmp[u] + weight) < distmp[v]:
                raise ValueError("negative cycle detected")
  
    return distmp


graph = {"A": {"B": -1, "C": 4}, "B": {"C": 3, "D": 2, "E": 2}, "C": {}, "D": {"B": 1, "C": 5}, "E": {"D": -3}}


# example of a negative cycle 'A' : {'A': -1}
print(bellman_ford(graph, "A"))
