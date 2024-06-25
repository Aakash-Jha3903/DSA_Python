def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = None
        min_distance = float('infinity')
        
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]
        
        visited.add(min_node)
        
        for neighbor, weight in graph[min_node].items():
            if neighbor not in visited:
                distance = distances[min_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print(f"Shortest distances from {start_node}: {distances}")
