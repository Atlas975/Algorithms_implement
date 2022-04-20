class Graph:
    def __init__(self):
        self.nodes = {}

    def add(self, new_key, edges = None, data = None, visit_cost = 0, add_type = "undirected"):
        if new_key in self.nodes.keys():
            self.nodes[new_key].edges.update(edges)
            self.nodes[new_key].data = data
            self.nodes[new_key].visit_cost = visit_cost
        else:
            self.nodes[new_key] = Node(new_key, edges, data, visit_cost)

        if(add_type[0].lower() == "u" and self.nodes[new_key].edges):
            for key in self.nodes[new_key].edges:
                if key in self.nodes.keys():
                    self.nodes[key].edges[new_key] = self.nodes[new_key].edges[key]
                else:
                    self.nodes[key] = Node(key, {new_key:self.nodes[new_key].edges[key]}, None, 0)

    def remove_node(self, removal_key):
        lost_data = self.nodes.pop(removal_key).data
        for key in self.nodes:
            if removal_key in self.nodes[key].edges:
                self.nodes[key].edges.pop(removal_key)
        return lost_data

    def remove_edge(self, node1, node2, removal_type = "undirected"):
        self.nodes[node1].edges.pop(node2)
        if(removal_type[0].lower() == "u"):
            self.nodes[node2].edges.pop(node1)

    def __repr__(self):
        for i in range(0, 28, 2):
            print(i+"")


    def shortest_path(self, start, target = None, visualize = False):
        distances = {node:(None, float('inf')) for node in self.nodes.keys()}
        distances.pop(start)
        visited = {start:(start, 0)}

        while len(distances) != 0:
            for traversed in visited.keys():
                for connection in self.nodes[traversed].edges:
                    if connection not in visited.keys():
                        route = visited[traversed][1] + self.nodes[traversed].edges[connection]
                        if(route < distances[connection][1]):
                            distances[connection] = (traversed, route)
            shortest = (None, float('inf'))
            destination = None
            for node in distances.keys():
                if (distances[node][1] < shortest[1]):
                    shortest = distances[node]
                    destination = node
            visited[destination] = shortest
            distances.pop(destination)

        if(visualize and target):
            path_visual = ""
            active = target
            while active != start:
                previous = visited[active][0]
                cost = visited[active][1]-visited[previous][1]
                path_visual = f'{previous} -{cost}- > '+path_visual
                active = previous
            path_visual = path_visual+target
            print(path_visual)
            print(f"Lowest cost of {start} --  > {target} = {visited[target][1]}\n")

        if(target):
            return visited[target]
        return visited

    def minimum_spanning_tree(self, return_weight = False):
        distances = {node:(None, float('inf')) for node in self.nodes.keys()}
        start, _ = distances.popitem()
        visited = {start:(start, 0)}

        while len(distances) != 0:
            for traversed in visited.keys():
                for connection in self.nodes[traversed].edges:
                    if connection not in visited.keys():
                        route = visited[traversed][1] + self.nodes[traversed].edges[connection]
                        if(route < distances[connection][1]):
                            distances[connection] = (traversed, route)
            shortest = (None, float('inf'))
            destination = None
            for node in distances.keys():
                if (distances[node][1] < shortest[1]):
                    shortest = distances[node]
                    destination = node
            visited[destination] = shortest
            distances.pop(destination)


        min_tree = {key: value[0] for key, value in visited.items()}
        if(return_weight):
            removed = min_tree.pop(start)
            total_weight = 0
            for edge in min_tree.keys():
                total_weight += self.nodes[edge].edges[min_tree[edge]]
            min_tree[removed] = removed
            return min_tree, total_weight
        return min_tree

    def __str__(self):
        metadata = "Graph metadata:\n"
        for node in self.nodes.values():
            metadata += " --  --  --  --  --  --  -- \n"
            metadata += f"Node: {node.key}\n"
            metadata += f"Edges: {node.edges}\n"
            metadata += f"Data: {node.data}\n"
            metadata += f"Visit cost: {node.visit_cost}\n"
        return metadata


class Node:
    def __init__(self, key, edges = None, data = None, visit_cost = 0):
        self.key = key
        self.edges = edges
        self.data = data
        self.visit_cost = visit_cost


