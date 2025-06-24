import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = set()
    queue = [(0, start)]

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if curr_node in visited:
            continue
        visited.add(curr_node)

        for neighbor in graph.neighbors(curr_node):
            weight = graph[curr_node][neighbor].get('weight', 1)
            new_distance = curr_dist + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances
