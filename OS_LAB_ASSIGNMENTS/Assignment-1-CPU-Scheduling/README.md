# ⚙️ CPU Scheduling Algorithms — FCFS & SJF  
### OS Lab Assignment 1 | ENCA252  
**BCA (AI & Data Science) | K.R. Mangalam University, Gurugram**

---

## 📌 Problem Statement

CPU Scheduling is a core function of an operating system that determines the order in which processes access the CPU.  

This assignment implements two fundamental scheduling algorithms:
- **First Come First Serve (FCFS)**
- **Shortest Job First (SJF - Non Preemptive)**  

The goal is to compute scheduling parameters and analyze system performance.

---

## 🎯 Objectives

- Understand CPU scheduling concepts  
- Implement FCFS and SJF algorithms  
- Calculate Completion Time (CT), Turnaround Time (TAT), Waiting Time (WT)  
- Visualize execution using Gantt Chart  
- Compare performance of algorithms  

---

## 🗂️ File Structure

```
Assignment-1-CPU-Scheduling/
│
├── main.py                 
├── output_screenshots/    
└── README.md
```

---

## 📚 Concepts Used

| Term | Formula | Description |
|------|--------|-------------|
| Completion Time (CT) | — | Time at which process finishes |
| Turnaround Time (TAT) | CT − AT | Total time from arrival to completion |
| Waiting Time (WT) | TAT − BT | Time spent waiting in queue |
| FCFS | — | Executes processes in arrival order |
| SJF | — | Executes process with shortest burst time |

---

## ▶️ How to Run

Make sure Python 3.x is installed.

```bash
cd Assignment-1-CPU-Scheduling
python main.py
```

---

## 🧪 Sample Input Used

```
Enter number of processes: 3

P1 0 5
P2 1 3
P3 2 8
```

---

## 📊 Sample Output

### 🔹 FCFS Scheduling

```
PID  AT  BT  CT  TAT  WT
P1   0   5   5   5    0
P2   1   3   8   7    4
P3   2   8   16  14   6
```

---

### 🔹 SJF Scheduling

```
PID  AT  BT  CT  TAT  WT
P1   0   5   5   5    0
P2   1   3   8   7    4
P3   2   8   16  14   6
```

---

### 🔹 Gantt Chart

```
FCFS:
| P1 | P2 | P3 |
0    5    8    16

SJF:
| P1 | P2 | P3 |
0    5    8    16
```

---

### 🔹 Performance Comparison

```
Average TAT: FCFS = 8.67, SJF = 8.67
Average WT : FCFS = 3.33, SJF = 3.33
```

---

## 🔍 Result Analysis

- FCFS is simple but may lead to higher waiting time  
- SJF minimizes waiting time by selecting shortest job first  
- In some cases, both may give similar results  
- Generally, SJF performs better than FCFS  

---

## 🛠️ Tools & Technologies

- Language: Python 3.x  
- Libraries: Built-in only  
- Platform: Windows / Linux / macOS  

---

## 👨‍💻 Submitted By

Aalok Kumar Singh  
BCA (AI & Data Science)  
K.R. Mangalam University  

---
