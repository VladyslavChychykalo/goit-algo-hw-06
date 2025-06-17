import networkx as nx


def build_graph():
    G = nx.Graph()
    stations = ["A", "B", "C", "D", "E", "F"]
    routes = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"),
              ("C", "E"), ("D", "F"), ("E", "F")]
    G.add_nodes_from(stations)
    G.add_edges_from(routes)
    return G


def create_weighted_graph():
    G = nx.Graph()
    stations = ["A", "B", "C", "D", "E", "F"]
    G.add_nodes_from(stations)
    routes = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "E", 8),
        ("D", "F", 6),
        ("E", "F", 3)
    ]
    for u, v, w in routes:
        G.add_edge(u, v, weight=w)
    return G
