import json
from collections import defaultdict
from src.network_utils import compute_edge_cost


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

    """
    def update_edge_load(self, source, target, load):
        for edge in self.edges:

            # find matching edge
            if (
                (edge["source"] == source and edge["target"] == target)
                or
                (edge["source"] == target and edge["target"] == source)
            ):

                # update congestion/load
                edge["attributes"]["current_load"] = load

                # recompute edge cost
                edge["cost"] = compute_edge_cost(edge["attributes"])

        # rebuild adjacency list with updated costs
        self.adj_list = defaultdict(list)

        for edge in self.edges:
            s = edge["source"]
            t = edge["target"]
            c = edge["cost"]

            self.adj_list[s].append((t, c))
            self.adj_list[t].append((s, c))
    """

    def update_edge_load(self, source, target, load):
        for edge in self.edges:
            if (
                (edge["source"] == source and edge["target"] == target)
                or
                (edge["source"] == target and edge["target"] == source)
                ):
                
                # get current load (default = 0)
                current = edge["attributes"].get("current_load", 0)

                # accumulate load instead of overwrite
                new_load = current + load
                edge["attributes"]["current_load"] = new_load

                # recompute cost
                edge["cost"] = compute_edge_cost(edge["attributes"])

    # rebuild adjacency list
        self.adj_list = defaultdict(list)

        for edge in self.edges:
            s = edge["source"]
            t = edge["target"]
            c = edge["cost"]

            self.adj_list[s].append((t, c))
            self.adj_list[t].append((s, c))        

    def decay_load(self, decay_factor=0.9):
        for edge in self.edges:
            current = edge["attributes"].get("current_load", 0)

            # reduce load gradually
            new_load = current * decay_factor
            edge["attributes"]["current_load"] = new_load

            # recompute cost
            edge["cost"] = compute_edge_cost(edge["attributes"])

        # rebuild adjacency list
        self.adj_list = defaultdict(list)

        for edge in self.edges:
            s = edge["source"]
            t = edge["target"]
            c = edge["cost"]

            self.adj_list[s].append((t, c))
            self.adj_list[t].append((s, c))

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")