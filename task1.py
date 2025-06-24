import matplotlib.pyplot as plt
import networkx as nx
from graph_builder import build_graph

G = build_graph()

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray')
plt.title("Візуалізація графа")
plt.show()

# 🔍 АНАЛІЗ ХАРАКТЕРИСТИК ГРАФА
print("- Кількість вершин:", G.number_of_nodes())
print("- Кількість ребер:", G.number_of_edges())

print("\n- Ступінь кожної вершини:")
for node, degree in G.degree():
    print(f"  Вершина {node}: ступінь {degree}")

print("\n- Щільність графа:", nx.density(G))

is_connected = nx.is_connected(G)
print("- Граф є зв'язним?" , "Так" if is_connected else "Ні")