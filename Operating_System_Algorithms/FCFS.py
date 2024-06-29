def main():
    bt = []
    wt = []
    tat = []
    wtavg = 0
    tatavg = 0

    n = int(input("\nEnter the number of processes -- "))

    # Input burst times for each process
    for i in range(n):
        bt.append(int(input(f"Enter Burst Time for Process {i} -- ")))

    # Calculate waiting time and turnaround time
    wt.append(0)
    tat.append(bt[0])

    for i in range(1, n):
        wt.append(wt[i-1] + bt[i-1])
        tat.append(tat[i-1] + bt[i])

    # Calculate average waiting time and average turnaround time
    for i in range(n):
        wtavg += wt[i]
        tatavg += tat[i]

    wtavg /= n
    tatavg /= n


    print("\t PROCESS \tBURST TIME \t WAITING TIME\t TURNAROUND TIME")
    for i in range(n):
        print(f"\n\t P{i} \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]}")

    print(f"\nAverage Waiting Time -- {wtavg}")
    print(f"Average Turnaround Time -- {tatavg}")


if __name__ == "__main__":
    main()
