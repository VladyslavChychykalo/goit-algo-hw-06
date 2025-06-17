import networkx as nx
import matplotlib.pyplot as plt
from graph_builder import create_weighted_graph


def run_dijkstra():
    G = create_weighted_graph()

    print("Найкоротші шляхи між усіма вершинами:")
    for source in G.nodes:
        lengths = nx.single_source_dijkstra_path_length(G, source)
        for target, distance in lengths.items():
            print(f"  {source} → {target}: {distance}")

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=12)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
    plt.title("Візуалізація графа з вагами")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_dijkstra()
