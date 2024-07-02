class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority)
    
    processes[0].waiting_time = 0
    processes[0].turnaround_time = processes[0].burst_time
    
    for i in range(1, len(processes)):
        processes[i].waiting_time = processes[i - 1].waiting_time + processes[i - 1].burst_time
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time

def main():
    n = int(input("Enter the number of processes: "))
    processes = []
    
    for i in range(n):
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        priority = int(input(f"Enter priority for process {i + 1}: "))
        processes.append(Process(i + 1, burst_time, priority))
    
    priority_scheduling(processes)
    
    total_waiting_time = 0
    total_turnaround_time = 0
    
    print("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t{process.burst_time}\t\t{process.priority}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time
    
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    
    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

if __name__ == "__main__":
    main()
