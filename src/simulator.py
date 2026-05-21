import random
from algorithms.dijkstra import dijkstra, get_path


def simulate_traffic(graph, num_packets=20,dynamic=True):
    nodes = list(graph.nodes.keys())

    count = 0
    packet_id = 1

    total_cost = 0
    successful_packets = 0

    while count < num_packets:
        src = random.choice(nodes)
        dst = random.choice(nodes)

        if src == dst:
            continue

        distances, prev = dijkstra(graph, src)
        path = get_path(prev, src, dst)

        if not path:
            continue

        cost = distances[dst]

        print(f"\nPacket {packet_id}: {src} -> {dst}")
        print("Path:", path)
        print("Path Cost:", round(cost, 2))

        total_cost += cost
        successful_packets += 1

        # apply load
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]

            load = random.randint(10, 50)
            if dynamic :
                graph.update_edge_load(u, v, load)

            print(f"Updated load on ({u}, {v}) = {load}")

        # apply decay
        if dynamic:
            graph.decay_load(decay_factor=0.9)

        count += 1
        packet_id += 1

    # metric calculations 
    print("\n===== SIMULATION SUMMARY =====")

    if successful_packets > 0:
        avg_cost = total_cost / successful_packets
        print("Total packets:", successful_packets)
        print("Average path cost:", round(avg_cost, 2))
    else:
        print("No successful packets.")

    # compute average congestion
    total_load = 0
    edge_count = 0

    for edge in graph.edges:
        load = edge["attributes"].get("current_load", 0)
        total_load += load
        edge_count += 1

    if edge_count > 0:
        avg_load = total_load / edge_count
        print("Average network load:", round(avg_load, 2))

    print("================================")