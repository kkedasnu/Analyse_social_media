import networkx as nx
import numpy as np

def calc_cntr_vect_centrality(G):
    # Для заданного графа
    try:
        centrality = nx.eigenvector_centrality_numpy(G)
        print("Centrality:")
        sorted_centrality = sorted(centrality.items(), key=lambda item: item[1], reverse=True)
        for node, value in sorted_centrality:
            print(f"Node {node}: {value:.4f}")
    except nx.PowerIterationFailedConvergence:
        print("Power iteration failed to converge. The graph might be disconnected or have other issues.")

# Manually designed graph (refined)
G = nx.Graph()
G.add_nodes_from(range(21))

# Create a central node (node 10) and connect it to most other nodes
for i in range(21):
    if i != 10 and i != 0 and i != 20:
        G.add_edge(10, i)

# Add some additional connections to create the desired pattern
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(6, 7)
G.add_edge(18, 19)

# Add connections around node 10
G.add_edge(8, 9)
G.add_edge(9, 10)
G.add_edge(10, 11)
G.add_edge(11, 12)

# Calculate and print centrality
calc_cntr_vect_centrality(G)