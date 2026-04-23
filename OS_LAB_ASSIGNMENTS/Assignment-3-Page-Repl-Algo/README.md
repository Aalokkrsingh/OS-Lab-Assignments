# 📄 Page Replacement Algorithms — Virtual Memory Management  
### OS Lab Assignment 3 | ENCA252  
**BCA (AI & Data Science) | K.R. Mangalam University, Gurugram**

---

## 📌 Problem Statement

In modern operating systems, virtual memory allows efficient utilization of physical memory. When memory frames are full, page replacement algorithms are used to decide which page should be replaced.

This assignment implements and analyzes multiple page replacement algorithms:
- FIFO (First-In-First-Out)
- LRU (Least Recently Used)
- Optimal
- MRU (Most Recently Used)
- Second Chance (Clock Algorithm)

The goal is to minimize **page faults** and compare algorithm efficiency.

---

## 🎯 Objectives

- Understand virtual memory and paging  
- Implement multiple page replacement algorithms  
- Calculate page faults  
- Compare performance of algorithms  
- Analyze efficiency and behavior  

---

## 🗂️ File Structure
Assignment-3-Page-Replacement/\
│\
├── main.py\
├── output_screenshots/\
└── README.md\


---

## 📚 Concepts Used

| Term | Description |
|------|-------------|
| Page | A unit of memory |
| Frame | Slot in physical memory |
| Page Fault | When requested page is not in memory |
| FIFO | Oldest page replaced first |
| LRU | Least recently used page replaced |
| Optimal | Page replaced based on future use |
| MRU | Most recently used page replaced |
| Second Chance | FIFO with reference bit improvement |

---

## ▶️ How to Run

Make sure Python 3.x is installed.

```bash
#Page Replacement Algorithms

def fifo(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
    return faults


def lru(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                lru_page = min(memory, key=lambda x: pages[:i][::-1].index(x))
                memory.remove(lru_page)
                memory.append(pages[i])
            faults += 1
    return faults


def optimal(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                replace = -1
                farthest = -1

                for m in memory:
                    if m not in future:
                        replace = m
                        break
                    else:
                        idx = future.index(m)
                        if idx > farthest:
                            farthest = idx
                            replace = m

                memory.remove(replace)
                memory.append(pages[i])
            faults += 1
    return faults


def mru(pages, frames):
    memory = []
    faults = 0
    recent = []

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.remove(recent[-1])
                memory.append(page)
            faults += 1
        if page in recent:
            recent.remove(page)
        recent.append(page)

    return faults


def second_chance(pages, frames):
    memory = []
    ref = []
    pointer = 0
    faults = 0

    for page in pages:
        if page not in memory:
            while len(memory) == frames and ref[pointer] == 1:
                ref[pointer] = 0
                pointer = (pointer + 1) % frames

            if len(memory) < frames:
                memory.append(page)
                ref.append(1)
            else:
                memory[pointer] = page
                ref[pointer] = 1
                pointer = (pointer + 1) % frames

            faults += 1
        else:
            ref[memory.index(page)] = 1

    return faults


# ---------------- INPUT ----------------
frames = int(input("Enter number of frames: "))
pages = list(map(int, input("Enter page reference string: ").split()))

# ---------------- OUTPUT ----------------
print("\nPage Faults:")

print("FIFO:", fifo(pages, frames))
print("LRU:", lru(pages, frames))
print("Optimal:", optimal(pages, frames))
print("MRU:", mru(pages, frames))
print("Second Chance:", second_chance(pages, frames))
cd Assignment-3-Page-Replacement
```

python main.py\
🧪 Sample Input\
Enter number of frames: 3\
Enter page reference string: 7 0 1 2 0 3 0 4 2 3 0 3\
📊 Sample Output\
Page Faults:\

FIFO: 9\
LRU: 8\
Optimal: 7\
MRU: 10\
Second Chance: 9\

📈 Performance Comparison\
Algorithm	Page Faults\
FIFO	9\
LRU	8\
Optimal	7 ✅ (Best)\
MRU	10 ❌\
Second Chance	9

🔍 Result Analysis
- Optimal Algorithm gives minimum page faults (best performance)
- LRU performs well and is widely used in real systems
- FIFO is simple but less efficient
- MRU is rarely useful and gives higher faults
- Second Chance improves FIFO using reference bits

👉 Conclusion:\
Optimal is best theoretically, but LRU is most practical.

🛠️ Tools & Technologies

Language: Python 3.x\
Libraries: Built-in only\
Platform: Windows / Linux / macOS

👨‍💻 Submitted By

Aalok Singh\
BCA (AI & Data Science)\
K.R. Mangalam University