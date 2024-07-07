# Implementing the Resource Allocation Graph (RAG) algorithm.

def main():
    np = int(input("Enter the number of processes: "))
    nr = int(input("Enter the number of resources: "))

    r = [int(input(f"Total amount of resource R{i + 1}: ")) for i in range(nr)]

    print("\nEnter the request matrix:")
    request = [[int(input()) for _ in range(nr)] for _ in range(np)]

    print("\nEnter the allocation matrix:")
    alloc = [[int(input()) for _ in range(nr)] for _ in range(np)]

    # Available resource calculation
    avail = [r[j] - sum(alloc[i][j] for i in range(np)) for j in range(nr)]

    # Marking processes with zero allocation
    mark = [all(alloc[i][j] == 0 for j in range(nr)) for i in range(np)]

    # Initialize W with available resources
    w = avail.copy()

    # Mark processes with requests less than or equal to W
    for i in range(np):
        if not mark[i] and all(request[i][j] <= w[j] for j in range(nr)):
            mark[i] = True
            w = [w[j] + alloc[i][j] for j in range(nr)]

    # Checking for unmarked processes
    deadlock = any(not mark[i] for i in range(np))

    if deadlock:
        print("\nDeadlock detected")
    else:
        print("\nNo Deadlock possible")

if __name__ == "__main__":
    main()




