
class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


def calculate_times(processes):
    n = len(processes)
    total_waiting_time = 0
    total_turnaround_time = 0
    
    processes.sort(key=lambda x: x.burst_time)
    
    for i in range(n):
        if i == 0:
            processes[i].waiting_time = 0
        else:
            processes[i].waiting_time = processes[i-1].waiting_time + processes[i-1].burst_time
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time
        
        total_waiting_time += processes[i].waiting_time
        total_turnaround_time += processes[i].turnaround_time
    
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    
    for process in processes:
        print(f"Process {process.name}: Waiting time = {process.waiting_time:.2f} ms, Turnaround time = {process.turnaround_time:.2f} ms")
    print(f"Average waiting time = {avg_waiting_time:.2f} ms")
    print(f"Average turnaround time = {avg_turnaround_time:.2f} ms")

processes = [Process("P1", 10), Process("P2", 5), Process("P3", 8)]

calculate_times(processes)