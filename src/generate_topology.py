import json
import random


def generate_topology(num_nodes=50):
    nodes = []
    edges = []

    # Step 1: Create nodes
    for i in range(1, num_nodes + 1):
        if i <= 5:
            node_type = "core"
        elif i <= 20:
            node_type = "distribution"
        else:
            node_type = "edge"

        nodes.append({
            "id": f"R{i}",
            "type": node_type
        })

    # Step 2: Create edges (to connect nodes)
    for i in range(1, num_nodes + 1):
        connections = random.randint(2, 4)

        for _ in range(connections):
            target = random.randint(1, num_nodes)

            if target == i:
                continue

            edge = {
                "source": f"R{i}",
                "target": f"R{target}",
                "latency": random.randint(5, 50),
                "bandwidth": random.choice([50, 100, 200, 500, 1000]),
                "packet_loss": round(random.uniform(0.001, 0.02), 4)
            }

            edges.append(edge)

    return {
        "nodes": nodes,
        "edges": edges
    }


def save_topology():
    topology = generate_topology(50)

    with open("../topologies/medium.json", "w") as f:
        json.dump(topology, f, indent=2)

    print(" medium.json generated!")


if __name__ == "__main__":
    save_topology()