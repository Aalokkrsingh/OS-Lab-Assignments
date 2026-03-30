# 🏦 Banker's Algorithm — Deadlock Avoidance  
### OS Lab Assignment 2 | ENCA252  
**BCA (AI & Data Science) | K.R. Mangalam University, Gurugram**

---

## 📌 Problem Statement

Deadlock is a situation in operating systems where a set of processes are unable to proceed because each is waiting for resources held by others.  

This assignment implements the **Banker's Algorithm** — a deadlock avoidance technique that ensures the system always remains in a **safe state** before allocating resources.

---

## 🎯 Objectives

- Understand resource allocation in operating systems  
- Implement Banker's Algorithm in Python  
- Calculate the **Need Matrix**  
- Determine whether the system is in a **Safe or Unsafe state**  
- Find the **Safe Sequence** of process execution  

---

## 🗂️ File Structure

```
Assignment-2-Bankers-Algorithm/
│
├── bankers.py                  
├── output_screenshots/        
└── README.md
```

---

## 📚 Concepts Used

| Term | Formula | Description |
|------|--------|-------------|
| Allocation Matrix | — | Resources currently held by each process |
| Maximum Matrix | — | Maximum resources a process may ever need |
| Need Matrix | Max − Allocation | Remaining resources required |
| Available Vector | — | Resources currently free |
| Work Vector | Work + Allocation | Simulated available resources |

---

## ▶️ How to Run

Make sure Python 3.x is installed.

```bash
cd Assignment-2-Bankers-Algorithm
python bankers.py
```

---

## 🧪 Sample Input Used

Processes: 5  
Resource Types: 3 (R0, R1, R2)

### Allocation Matrix

```
     R0  R1  R2
P0 [  0   1   0 ]
P1 [  2   0   0 ]
P2 [  3   0   2 ]
P3 [  2   1   1 ]
P4 [  0   0   2 ]
```

### Maximum Matrix

```
     R0  R1  R2
P0 [  7   5   3 ]
P1 [  3   2   2 ]
P2 [  9   0   2 ]
P3 [  2   2   2 ]
P4 [  4   3   3 ]
```

### Available Resources

```
[ 3   3   2 ]
```

---

## 📊 Sample Output

### Need Matrix (Max − Allocation)

```
     R0  R1  R2
P0 [  7   4   3 ]
P1 [  1   2   2 ]
P2 [  6   0   0 ]
P3 [  0   1   1 ]
P4 [  4   3   1 ]
```

---

### Safety Algorithm Trace

```
Step 1 → P1  |  Work: [3,3,2] + Alloc: [2,0,0] = [5,3,2]
Step 2 → P3  |  Work: [5,3,2] + Alloc: [2,1,1] = [7,4,3]
Step 3 → P0  |  Work: [7,4,3] + Alloc: [0,1,0] = [7,5,3]
Step 4 → P2  |  Work: [7,5,3] + Alloc: [3,0,2] = [10,5,5]
Step 5 → P4  |  Work: [10,5,5] + Alloc: [0,0,2] = [10,5,7]
```

---

### System State

```
SAFE STATE
```

### Safe Sequence

```
P1 -> P3 -> P0 -> P2 -> P4
```

---

## 🔍 Result Analysis

The system is in a **SAFE STATE** because a valid safe sequence exists.  

Each process in the sequence can:
- Obtain required resources  
- Execute successfully  
- Release resources  

This ensures that no deadlock occurs.

Banker's Algorithm guarantees that if a safe sequence exists, the system will remain deadlock-free.
 
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
