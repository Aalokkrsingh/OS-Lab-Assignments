# 💽 Disk Scheduling Algorithms — Seek Time Optimization  
OS Lab Assignment 4 | ENCA252  
BCA (AI & Data Science) | K.R. Mangalam University, Gurugram  

---

## 📌 Problem Statement  

Disk scheduling is an essential function of operating systems that determines the order in which disk I/O requests are serviced. Efficient scheduling reduces seek time and improves system performance.  

This assignment implements multiple disk scheduling algorithms to optimize disk head movement and minimize total seek time.  

---

## 🎯 Objectives  

Understand disk scheduling concepts  
Implement disk scheduling algorithms in Python  
Calculate total seek time  
Compare performance of different algorithms  
Analyze system efficiency  

---

## 🗂️ File Structure  

Assignment-4-Disk-Scheduling/  
│  
├── disk_scheduling.py  
├── output_screenshots/  
└── README.md  

---

## 📚 Concepts Used  

| Term | Description |
|------|-------------|
| Disk Request | Request for disk access |
| Seek Time | Time taken by head movement |
| Head Movement | Movement of disk arm |
| FCFS | Serves requests in arrival order |
| SSTF | Serves nearest request first |
| SCAN | Moves like elevator |
| C-SCAN | Moves in one direction only |

---

## ▶️ How to Run  

cd Assignment-4-Disk-Scheduling\
python disk_scheduling.py

---

## 🧪 Sample Input Used  

Disk Requests:  
98 183 37 122 14 124 65 67  

Initial Head Position: 53  

Disk Size: 200  

---

## 📊 Sample Output  

Total Seek Time:  

FCFS: 640  
SSTF: 236  
SCAN: 331  
C-SCAN: 382  

---

## 📈 Performance Comparison  

| Algorithm | Seek Time |
|----------|----------|
| FCFS     | 640 ❌ |
| SSTF     | 236 ✅ Best |
| SCAN     | 331 |
| C-SCAN   | 382 |

---

## 🔍 Result Analysis  

SSTF provides the minimum seek time and best performance in most cases.  

SCAN offers balanced performance by servicing requests in both directions.  

C-SCAN ensures uniform waiting time for all requests.  

FCFS is simple but inefficient due to higher seek time.  

---

## 🛠️ Tools & Technologies  

Language: Python 3.x  
Libraries: Built-in only  
Platform: Windows / Linux / macOS  

---

## 👨‍💻 Submitted By  

Aalok Kumar Singh  
BCA (AI & Data Science)  
K.R. Mangalam University  

Make sure Python 3.x is installed.  
