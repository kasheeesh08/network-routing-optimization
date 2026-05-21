import random
from algorithms.dijkstra import dijkstra, get_path


def simulate_traffic(graph, num_packets=20):
    nodes = list(graph.nodes.keys())

    count = 0
    packet_id = 1

    while count < num_packets:
        # random source and destination
        src = random.choice(nodes)
        dst = random.choice(nodes)

        # skip same node case
        if src == dst:
            continue

        # compute shortest path
        distances, prev = dijkstra(graph, src)
        path = get_path(prev, src, dst)

        # skip if no path found
        if not path:
            continue

        print(f"\nPacket {packet_id}: {src} -> {dst}")
        print("Path:", path)

        # simulate congestion on used edges
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]

            # random load
            load = random.randint(10, 50)

            # update edge load
            graph.update_edge_load(u, v, load)

            print(f"Updated load on ({u}, {v}) = {load}")
        
        # NEW: decay after each packet
        graph.decay_load(decay_factor=0.9)
        
        count += 1
        packet_id += 1