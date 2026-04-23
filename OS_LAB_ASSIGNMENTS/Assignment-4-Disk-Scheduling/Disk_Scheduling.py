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