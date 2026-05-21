# 🚀 Network Routing Optimization using Dynamic Congestion-Aware Algorithms

---

# 📌 Overview

This project simulates a network routing system that dynamically adapts to congestion using graph algorithms.

It compares:

- 📍 Static Routing (fixed shortest path)
- 🔁 Dynamic Routing (congestion-aware adaptive routing)

The system models realistic network conditions including:

- Latency
- Bandwidth
- Packet loss
- Traffic congestion

---

# 🧠 Key Idea

Traditional shortest-path routing does not consider real-time network conditions.

This project introduces a multi-objective cost function:

```python
Cost = f(latency, bandwidth, packet_loss, congestion)
```

👉 This allows routing decisions to adapt dynamically based on network load.

---

# 🏗️ Project Structure

```text
network-routing-optimization/
│
├── src/
│   ├── graph.py              # Graph structure + dynamic updates
│   ├── network_utils.py      # Cost function logic
│   ├── simulator.py          # Traffic simulation engine
│   ├── experiment.py         # Static vs Dynamic comparison
│
├── algorithms/
│   ├── dijkstra.py           # Shortest path algorithm
│
├── topologies/
│   ├── small.json            # Manual network
│   ├── medium.json           # Generated network
│
├── README.md
```

---

# ⚙️ Features

- ✅ Graph-based network modeling
- ✅ Dijkstra shortest path algorithm
- ✅ Multi-objective cost function
- ✅ Dynamic congestion updates
- ✅ Load accumulation + decay
- ✅ Traffic simulation (multiple packets)
- ✅ Performance metrics tracking
- ✅ Static vs Dynamic routing comparison

---

# 🧪 How It Works

## 1. Network Modeling

Nodes represent routers:
- Core
- Distribution
- Edge

Edges contain:
- Latency
- Bandwidth
- Packet loss

---

## 2. Cost Function

Each edge cost is computed as:

```python
cost = (
    α * latency +
    β * (1 / bandwidth) +
    γ * packet_loss +
    δ * congestion
)
```

---

## 3. Dynamic Routing

- Traffic increases edge load
- Load accumulates over time
- Load decays gradually
- Routes adapt based on updated cost

---

## 4. Simulation

- Random packets generated
- Shortest path computed
- Congestion updated dynamically
- Metrics recorded

---

# 📊 Results (Sample Output)

| Metric | Static Routing | Dynamic Routing |
|---|---|---|
| Avg Path Cost | 40.34 | 24.42 ✅ |
| Avg Network Load | 55.14 | 35.22 ✅ |

---

# 🔥 Key Findings

- Static routing creates congestion hotspots
- Dynamic routing distributes traffic efficiently

### Achieved:
- ⚡ ~39% reduction in path cost
- 📉 ~36% reduction in network load

---

# 🧠 Conclusion

Dynamic congestion-aware routing:

- Improves overall network efficiency
- Reduces bottlenecks
- Adapts to changing traffic conditions

This demonstrates how incorporating real-time metrics into routing decisions leads to significantly better performance than traditional static approaches.
