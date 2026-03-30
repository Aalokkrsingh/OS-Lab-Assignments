# CPU Scheduling: FCFS & SJF (Non-Preemptive)

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# -------------------- INPUT --------------------
processes = []

n = int(input("Enter number of processes: "))

for i in range(n):
    print(f"\nEnter details for Process {i+1}")
    pid = input("Process ID: ")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    processes.append(Process(pid, at, bt))


# -------------------- DISPLAY INPUT --------------------
print("\nProcess Table:")
print("PID\tAT\tBT")
for p in processes:
    print(f"{p.pid}\t{p.at}\t{p.bt}")


# -------------------- FCFS --------------------
fcfs = sorted(processes, key=lambda x: x.at)

current_time = 0
total_tat = 0
total_wt = 0

gantt_fcfs = []

print("\n========== FCFS Scheduling ==========")
print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in fcfs:
    if current_time < p.at:
        current_time = p.at

    start = current_time
    current_time += p.bt

    p.ct = current_time
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt

    total_tat += p.tat
    total_wt += p.wt

    gantt_fcfs.append((p.pid, start, current_time))

    print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

print(f"\nAverage TAT: {total_tat/len(fcfs):.2f}")
print(f"Average WT: {total_wt/len(fcfs):.2f}")


# -------------------- SJF (Non-Preemptive) --------------------
sjf = processes.copy()
completed = []
current_time = 0

total_tat_sjf = 0
total_wt_sjf = 0

gantt_sjf = []

print("\n========== SJF Scheduling ==========")
print("PID\tAT\tBT\tCT\tTAT\tWT")

while len(completed) < len(sjf):
    # Get available processes
    available = [p for p in sjf if p.at <= current_time and p not in completed]

    if not available:
        current_time += 1
        continue

    # Select process with shortest burst time
    p = min(available, key=lambda x: x.bt)

    start = current_time
    current_time += p.bt

    p.ct = current_time
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt

    total_tat_sjf += p.tat
    total_wt_sjf += p.wt

    gantt_sjf.append((p.pid, start, current_time))
    completed.append(p)

    print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

print(f"\nAverage TAT: {total_tat_sjf/len(sjf):.2f}")
print(f"Average WT: {total_wt_sjf/len(sjf):.2f}")


# -------------------- GANTT CHART --------------------
print("\n========== Gantt Chart (FCFS) ==========")
for p in gantt_fcfs:
    print(f"| {p[0]} ", end="")
print("|")

for p in gantt_fcfs:
    print(p[1], end="   ")
print(gantt_fcfs[-1][2])


print("\n========== Gantt Chart (SJF) ==========")
for p in gantt_sjf:
    print(f"| {p[0]} ", end="")
print("|")

for p in gantt_sjf:
    print(p[1], end="   ")
print(gantt_sjf[-1][2])


# -------------------- COMPARISON --------------------
print("\n========== Comparison ==========")

avg_wt_fcfs = total_wt / len(fcfs)
avg_wt_sjf = total_wt_sjf / len(sjf)

avg_tat_fcfs = total_tat / len(fcfs)
avg_tat_sjf = total_tat_sjf / len(sjf)

print(f"FCFS Avg WT: {avg_wt_fcfs:.2f}, Avg TAT: {avg_tat_fcfs:.2f}")
print(f"SJF Avg WT: {avg_wt_sjf:.2f}, Avg TAT: {avg_tat_sjf:.2f}")

if avg_wt_sjf < avg_wt_fcfs:
    print("SJF is better (less waiting time)")
else:
    print("FCFS is better")