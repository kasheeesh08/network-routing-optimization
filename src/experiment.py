from src.graph import Graph
from src.simulator import simulate_traffic


def run_static_simulation():
    print("\n===== STATIC ROUTING =====")

    g = Graph()
    g.load_from_json("topologies/small.json")

    # running without the congestion updates (baseline)
    simulate_traffic(g, num_packets=10)


def run_dynamic_simulation():
    print("\n===== DYNAMIC ROUTING =====")

    g = Graph()
    g.load_from_json("topologies/small.json")

    # Running with the congestion (my current system)
    simulate_traffic(g, num_packets=10)


if __name__ == "__main__":
    run_static_simulation()
    run_dynamic_simulation()