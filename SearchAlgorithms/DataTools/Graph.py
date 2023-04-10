from dataclasses import dataclass, field
from typing import Dict, Optional, Union


@dataclass
class Graph:
    nodes: Optional[Dict[str, "Node"]] = field(default_factory=dict)

    def add(self, new_key, edges=None, data=None, visit_cost=0, add_type="undirected"):
        if new_key in self.nodes.keys():
            self.nodes[new_key].edges.update(edges)
            self.nodes[new_key].data = data
            self.nodes[new_key].visit_cost = visit_cost
        else:
            self.nodes[new_key] = Node(new_key, edges, data, visit_cost)

        if add_type[0].lower() == "u" and self.nodes[new_key].edges:
            for key in self.nodes[new_key].edges:
                if key in self.nodes.keys():
                    self.nodes[key].edges[new_key] = self.nodes[new_key].edges[key]
                else:
                    self.nodes[key] = Node(key, {new_key: self.nodes[new_key].edges[key]}, None, 0)

    def remove_node(self, removal_key):
        lost_data = self.nodes.pop(removal_key).data
        for key in self.nodes:
            if removal_key in self.nodes[key].edges:
                self.nodes[key].edges.pop(removal_key)
        return lost_data

    def remove_edge(self, node1, node2, removal_type="undirected"):
        self.nodes[node1].edges.pop(node2)
        if removal_type[0].lower() == "u":
            self.nodes[node2].edges.pop(node1)

    def shortest_path(self, start, target=None, visualize=False):
        distances = {node: (None, float("inf")) for node in self.nodes.keys()}
        distances.pop(start)
        path = {start: (start, 0)}
        while distances:
            for traversed in path:
                for connection in self.nodes[traversed].edges:
                    if connection not in path.keys():
                        route = path[traversed][1] + self.nodes[traversed].edges[connection]
                        if route < distances[connection][1]:
                            distances[connection] = traversed, route
            shortest = (None, float("inf"))
            destination = None
            for node, value in distances.items():
                if value[1] < shortest[1]:
                    shortest = distances[node]
                    destination = node
            path[destination] = shortest
            distances.pop(destination)
        if visualize and target:
            path_visual = ""
            active = target
            while active != start:
                previous = path[active][0]
                cost = path[active][1] - path[previous][1]
                path_visual = f"{previous} -{cost}-> {path_visual}"
                active = previous
            path_visual = path_visual + target
            print(path_visual)
            print(f"Lowest cost of {start} --> {target} = {path[target][1]}\n")
        return path[target] if target else path

    def minimum_spanning_tree(self, start, target=None, visualize=False):
        pass

    def __str__(self):
        metadata = "Graph metadata:\n"
        for node in self.nodes.values():
            metadata += "--------------\n"
            metadata += f"Node: {node.key}\n"
            metadata += f"Edges: {node.edges}\n"
            metadata += f"Data: {node.data}\n"
            metadata += f"Visit cost: {node.visit_cost}\n"
        return metadata


@dataclass
class Node:
    key: str
    edges: Optional[Dict[str, int]] = field(default_factory=dict)
    data: Optional[object] = None
    visit_cost: Union[int, float] = 0


if __name__ == "__main__":
    graph = Graph()
    graph.add("a", {"b": 15, "d": 23, "i": 33})
    graph.add("b", {"e": 6, "c": 9})
    graph.add("c", {"d": 12})
    graph.add("d", {"e": 46, "g": 3, "i": 2})
    graph.add("e", {"f": 14, "h": 4})
    graph.add("i", {"j": 5})
    print(graph.shortest_path("b", "g", True))

# print(graph)4
