def warshall(graph, n):
    reach = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            reach[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    print("\nTransitive Closure:")
    for row in reach:
        print(row)

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    graph = []
    print("Enter the adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    # Example adjacency matrix
    # graph = [
    #     [1, 1, 0, 0],
    #     [0, 1, 1, 0],
    #     [0, 0, 1, 1],
    #     [0, 0, 0, 1]
    # ]

    warshall(graph, n)
