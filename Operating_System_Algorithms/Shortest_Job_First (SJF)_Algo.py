def SJF_Scheduling(processes):
    n = len(processes)
    total_waiting_time = 0
    total_turnaround_time = 0

    # Sort processes based on burst time (shortest job first)
    processes.sort(key=lambda x: x[1])

    # Calculate waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # First process has 0 waiting time
    waiting_time[0] = 0

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    # Calculate total waiting time and total turnaround time
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    # Calculate averages
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # Display results
    print("Process\t Burst Time\t Waiting Time\t Turnaround Time")
    for i in range(n):
        print(f"P{i}\t\t {processes[i][1]}\t\t {waiting_time[i]}\t\t {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")


# Example usage:
if __name__ == "__main__":
    
    # Example processes: (process_id, burst_time)
    processes = [
        (0, 6),
        (1, 8),
        (2, 7),
        (3, 3),
        (4, 4)
    ]
    
    SJF_Scheduling(processes)
