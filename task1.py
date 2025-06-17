import matplotlib.pyplot as plt
import networkx as nx
from graph_builder import build_graph

G = build_graph()

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray')
plt.title("Візуалізація графа")
plt.show()
