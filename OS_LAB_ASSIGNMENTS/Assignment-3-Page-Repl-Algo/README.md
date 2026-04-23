# 📄 Page Replacement Algorithms — Virtual Memory Management  
OS Lab Assignment 3 | ENCA252  
BCA (AI & Data Science) | K.R. Mangalam University, Gurugram  

---

## 📌 Problem Statement  

In modern operating systems, virtual memory allows efficient utilization of physical memory. When memory frames are full, page replacement algorithms are used to decide which page should be replaced.  

This assignment implements multiple page replacement algorithms to minimize page faults and improve memory efficiency.  

---

## 🎯 Objectives  

Understand virtual memory and paging concepts  
Implement page replacement algorithms in Python  
Calculate the number of page faults  
Compare performance of different algorithms  
Analyze system efficiency  

---

## 🗂️ File Structure  

Assignment-3-Page-Replacement/  
│  
├── main.py  
├── output_screenshots/  
└── README.md  

---

## 📚 Concepts Used  

| Term | Description |
|------|-------------|
| Page | A unit of memory |
| Frame | Slot in physical memory |
| Page Fault | Occurs when page is not in memory |
| FIFO | Oldest page replaced first |
| LRU | Least recently used page replaced |
| Optimal | Page replaced based on future use |
| MRU | Most recently used page replaced |
| Second Chance | FIFO with reference bit improvement |

---

## ▶️ How to Run  

cd Assignment-3-Page-Replacement
python main.py

---

## 🧪 Sample Input Used  

Number of Frames: 3  

Page Reference String:  
7 0 1 2 0 3 0 4 2 3 0 3  

---

## 📊 Sample Output  

Page Faults:  

FIFO: 9  
LRU: 8  
Optimal: 7  
MRU: 10  
Second Chance: 9  

---

## 📈 Performance Comparison  

| Algorithm | Page Faults |
|----------|------------|
| FIFO     | 9 |
| LRU      | 8 |
| Optimal  | 7 ✅ Best |
| MRU      | 10 ❌ |
| Second Chance | 9 |

---

## 🔍 Result Analysis  

Optimal algorithm gives the minimum number of page faults and is considered the best for performance.  

LRU is widely used in real systems as it provides a good balance between performance and implementation complexity.  

FIFO is simple but less efficient, while MRU generally performs poorly.  

Second Chance improves FIFO by reducing unnecessary replacements.  

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
