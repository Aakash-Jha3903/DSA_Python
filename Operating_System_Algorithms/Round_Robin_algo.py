def round_robin(processes, burst_times, time_slice):
    n = len(processes) 
    remaining_burst_times = burst_times[:]  # Copy of burst times
    waiting_times = [0] * n
    turnaround_times = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    
    current_time = 0  
    while True:
        done = True
        for i in range(n):
            if remaining_burst_times[i] > 0:
                done = False
                if remaining_burst_times[i] > time_slice:
                    current_time += time_slice
                    remaining_burst_times[i] -= time_slice
                else:
                    current_time += remaining_burst_times[i]
                    waiting_times[i] = current_time - burst_times[i]
                    remaining_burst_times[i] = 0

        if done:
            break

    for i in range(n):
        turnaround_times[i] = burst_times[i] + waiting_times[i]
        total_waiting_time += waiting_times[i]
        total_turnaround_time += turnaround_times[i]

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print(f"Processes    Burst Time    Waiting Time    Turnaround Time")
    for i in range(n):
        print(f"    {processes[i]}           {burst_times[i]}              {waiting_times[i]}               {turnaround_times[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

# Example run
processes = [1, 2, 3, 4]
burst_times = [5, 4, 3, 2]
time_slice = 2

round_robin(processes, burst_times, time_slice)