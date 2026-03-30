# Banker's Algorithm - Full Implementation

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

# Allocation Matrix
allocation = []
print("\nEnter Allocation Matrix:")
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

# Maximum Matrix
maximum = []
print("\nEnter Maximum Matrix:")
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    maximum.append(row)

# Available Resources
available = list(map(int, input("\nEnter Available Resources: ").split()))

# ---------------- NEED MATRIX ----------------
need = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("\nNeed Matrix:")
for row in need:
    print(row)

# ---------------- SAFETY ALGORITHM ----------------
work = available.copy()
finish = [False] * n
safe_sequence = []

while len(safe_sequence) < n:
    found = False

    for i in range(n):
        if not finish[i]:
            # Check if need <= work
            if all(need[i][j] <= work[j] for j in range(m)):
                
                # Add allocation to work
                for j in range(m):
                    work[j] += allocation[i][j]

                safe_sequence.append(f"P{i}")
                finish[i] = True
                found = True

    if not found:
        break

# ---------------- RESULT ----------------
if len(safe_sequence) == n:
    print("\nSystem is in SAFE state")
    print("Safe Sequence:", " -> ".join(safe_sequence))
else:
    print("\nSystem is in UNSAFE state (Deadlock possible)")