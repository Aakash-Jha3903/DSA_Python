# To implement deadlock prevention technique.(Banker‘s Algorithm)

import numpy as np

class BankersAlgorithm:
    def __init__(self, available, max_demand, allocation):
        self.available = np.array(available)
        self.max_demand = np.array(max_demand)
        self.allocation = np.array(allocation)
        self.num_processes = self.max_demand.shape[0]
        self.num_resources = self.available.shape[0]
        self.need = self.max_demand - self.allocation

    def is_safe_state(self):
        work = np.copy(self.available)
        finish = np.full(self.num_processes, False)
        safe_sequence = []

        while len(safe_sequence) < self.num_processes:
            allocated = False
            for i in range(self.num_processes):
                if not finish[i] and np.all(self.need[i] <= work):
                    work += self.allocation[i]
                    finish[i] = True
                    safe_sequence.append(i)
                    allocated = True
            if not allocated:
                return False, []
        
        return True, safe_sequence

    def request_resources(self, process_num, request):
        if np.any(request > self.need[process_num]):
            print(f"Error: Process {process_num} has exceeded its maximum claim.")
            return False
        
        if np.any(request > self.available):
            print(f"Error: Resources are not available for Process {process_num}.")
            return False
        
        self.available -= request
        self.allocation[process_num] += request
        self.need[process_num] -= request

        safe, _ = self.is_safe_state()
        if not safe:
            self.available += request
            self.allocation[process_num] -= request
            self.need[process_num] += request
            print(f"Process {process_num}'s request cannot be granted without risking deadlock.")
            return False

        print(f"Process {process_num}'s request has been granted.")
        return True

# Example usage
available_resources = [3, 3, 2]
max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

bankers = BankersAlgorithm(available_resources, max_demand, allocation)
print("Initial State:")
print(f"Available Resources: {bankers.available}")
print(f"Maximum Demand: \n{bankers.max_demand}")
print(f"Allocation: \n{bankers.allocation}")
print(f"Need: \n{bankers.need}")

process_num = 1
request = [1, 0, 2]
print(f"\nProcess {process_num} requesting resources {request}")
bankers.request_resources(process_num, request)

safe, safe_sequence = bankers.is_safe_state()
print(f"\nSystem is in a {'safe' if safe else 'unsafe'} state.")
if safe:
    print(f"Safe sequence: {safe_sequence}")
