# 💽 Disk Scheduling Algorithms — Seek Time Optimization  
### OS Lab Assignment 4 | ENCA252  
**BCA (AI & Data Science) | K.R. Mangalam University, Gurugram**

---

## 📌 Problem Statement

Disk scheduling is an essential function of operating systems that determines the order in which disk I/O requests are serviced. Efficient disk scheduling improves system performance by reducing seek time and increasing throughput.

This assignment implements and analyzes multiple disk scheduling algorithms:
- FCFS (First Come First Serve)  
- SSTF (Shortest Seek Time First)  
- SCAN (Elevator Algorithm)  
- C-SCAN (Circular SCAN)  

The goal is to minimize **total seek time** and compare algorithm efficiency.

---

## 🎯 Objectives

- Understand disk scheduling concepts  
- Implement various disk scheduling algorithms  
- Calculate total seek time  
- Compare performance of algorithms  
- Analyze system efficiency  

---

## 🗂️ File Structure
Assignment-4-Disk-Scheduling\
│\
├── disk_scheduling.py\
├── output_screenshots\
└── README.md

---

## ▶️ How to Run

```bash
#Disk Scheduling Algorithms

def fcfs(requests, head):
    seek = 0
    sequence = []

    for r in requests:
        seek += abs(head - r)
        head = r
        sequence.append(r)

    return seek, sequence


def sstf(requests, head):
    req = requests.copy()
    seek = 0
    sequence = []

    while req:
        nearest = min(req, key=lambda x: abs(x - head))
        seek += abs(head - nearest)
        head = nearest
        sequence.append(nearest)
        req.remove(nearest)

    return seek, sequence


def scan(requests, head, disk_size):
    seek = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    for r in right:
        seek += abs(head - r)
        head = r
        sequence.append(r)

    # move to end
    seek += abs(head - (disk_size - 1))
    head = disk_size - 1

    for r in left:
        seek += abs(head - r)
        head = r
        sequence.append(r)

    return seek, sequence


def cscan(requests, head, disk_size):
    seek = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    for r in right:
        seek += abs(head - r)
        head = r
        sequence.append(r)

    # jump to start
    seek += abs(head - (disk_size - 1))
    head = 0
    seek += disk_size - 1

    for r in left:
        seek += abs(head - r)
        head = r
        sequence.append(r)

    return seek, sequence


# ---------------- INPUT ----------------
requests = list(map(int, input("Enter disk requests: ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

# ---------------- OUTPUT ----------------
print("\nResults:\n")

seek, seq = fcfs(requests, head)
print("FCFS:")
print("Sequence:", seq)
print("Seek Time:", seek)

seek, seq = sstf(requests, head)
print("\nSSTF:")
print("Sequence:", seq)
print("Seek Time:", seek)

seek, seq = scan(requests, head, disk_size)
print("\nSCAN:")
print("Sequence:", seq)
print("Seek Time:", seek)

seek, seq = cscan(requests, head, disk_size)
print("\nC-SCAN:")
print("Sequence:", seq)
print("Seek Time:", seek)
```

🧪 Sample Input\
Enter disk requests: 98 183 37 122 14 124 65 67\
Enter initial head position: 53\
Enter disk size: 200

📊 Sample Output\
FCFS:\
Seek Time: 640

SSTF:\
Seek Time: 236

SCAN:\
Seek Time: 331

C-SCAN:\
Seek Time: 382

📈 Performance Comparison\
Algorithm	Seek Time\
FCFS	640 ❌\
SSTF	236 ✅ Best\
SCAN	331\
C-SCAN	382