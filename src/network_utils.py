def bandwidth_to_cost(bandwidth):
    """
    Higher bandwidth = lower cost
    """
    if bandwidth == 0:
        return float('inf')
    return 1 / bandwidth


def latency_cost(latency):
    """
    Direct latency cost
    """
    return latency


def packet_loss_cost(packet_loss):
    """
    Penalize unreliable links
    """
    return packet_loss * 100  # scale it

"""
def compute_edge_cost(edge):
    latency = latency_cost(edge["latency"])
    bandwidth = bandwidth_to_cost(edge["bandwidth"])
    loss = packet_loss_cost(edge["packet_loss"])

    # weights (will'be tuned later)
    return (
        0.6 * latency +
        0.3 * bandwidth +
        0.1 * loss
    )
"""

def compute_edge_cost(edge):
    latency = latency_cost(edge["latency"])
    bandwidth = bandwidth_to_cost(edge["bandwidth"])
    loss = packet_loss_cost(edge["packet_loss"])

    # NEW: congestion factor
    congestion = edge.get("current_load", 0)

    return (
        0.5 * latency +
        0.2 * bandwidth +
        0.1 * loss +
        0.2 * congestion
    )