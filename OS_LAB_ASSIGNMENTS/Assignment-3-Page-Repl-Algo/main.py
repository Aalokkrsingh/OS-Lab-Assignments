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