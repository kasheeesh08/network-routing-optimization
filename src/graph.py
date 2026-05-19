import json
from collections import defaultdict
from network_utils import compute_edge_cost


class Graph:
    def __init__(self):
        # adjacency list: node -> list of (neighbor, cost)
        self.adj_list = defaultdict(list)

        # store full edge info if needed later
        self.edges = []

        # store node metadata
        self.nodes = {}

    def add_node(self, node_id, node_type=None):
        self.nodes[node_id] = {
            "type": node_type
        }

    def add_edge(self, source, target, attributes):
        cost = compute_edge_cost(attributes)

        # undirected graph (important for networks)
        self.adj_list[source].append((target, cost))
        self.adj_list[target].append((source, cost))

        self.edges.append({
            "source": source,
            "target": target,
            "attributes": attributes,
            "cost": cost
        })

    def get_neighbors(self, node):
        return self.adj_list[node]

    def load_from_json(self, file_path):
        with open(file_path, "r") as f:
            data = json.load(f)

        # load nodes
        for node in data["nodes"]:
            self.add_node(node["id"], node.get("type"))

        # load edges
        for edge in data["edges"]:
            self.add_edge(
                edge["source"],
                edge["target"],
                {
                    "latency": edge["latency"],
                    "bandwidth": edge["bandwidth"],
                    "packet_loss": edge["packet_loss"]
                }
            )

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")