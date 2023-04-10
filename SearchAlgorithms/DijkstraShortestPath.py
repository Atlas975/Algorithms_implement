import heapq


def dijkstra(graph, origin) -> dict:  # O(ElogV) time, O(V) space
    distmp = {vertex: float("inf") for vertex in graph}
    distmp[origin] = 0
    pq = [(0, origin)]

    while pq:
        udist, u = heapq.heappop(pq)
        if udist > distmp[u]:
            continue
        for v, weight in graph[u].items():
            if (vdist := udist + weight) < distmp[v]:
                distmp[v] = vdist
                heapq.heappush(pq, (vdist, v))
    return distmp


graph = {
    "A": {"B": 2, "C": 1},
    "B": {"A": 2, "D": 3},
    "C": {"A": 1, "D": 1},
    "D": {"B": 3, "C": 1, "E": 5},
    "E": {"D": 5},
}
distances = dijkstra(graph, "A")
print(distances)
