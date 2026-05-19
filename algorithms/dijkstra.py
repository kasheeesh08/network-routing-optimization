import heapq


def dijkstra(graph, start):
    # distances from start node
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    # store previous node for path reconstruction
    previous = {node: None for node in graph.nodes}

    # min heap (priority queue)
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # skip outdated entries
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    # if start not reached
    if path[0] != start:
        return []

    return path