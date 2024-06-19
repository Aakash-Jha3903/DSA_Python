def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print("\nShortest Paths:")
    for row in dist:
        print(row)

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    graph = []
    print("Enter the adjacency matrix (use 'inf' for no path):")
    for i in range(n):
        row = input().split()
        for j in range(n):
            if row[j] == 'inf':
                row[j] = float('inf')
            else:
                row[j] = int(row[j])
        graph.append(row)

    # Example adjacency matrix
    # graph = [
    #     [0, 3, float('inf'), 7],
    #     [8, 0, 2, float('inf')],
    #     [5, float('inf'), 0, 1],
    #     [2, float('inf'), float('inf'), 0]
    # ]

    floyd_warshall(graph, n)
