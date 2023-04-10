from itertools import product


def floyd_warshall(graph):  # O(V^3) time, O(V^2) space
    dist = {u: {v: float("inf") for v in graph} for u in graph}

    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight
        dist[u][u] = 0

    for k, i, j in product(graph.keys(), repeat=3):
        if dist[i][j] > (weight := dist[i][k] + dist[k][j]):
            dist[i][j] = weight
    return dist


graph = {"A": {"C": -2}, "B": {"A": 4, "C": 3}, "C": {"D": 2}, "D": {"B": -1}, "E": {}}

print(floyd_warshall(graph))
