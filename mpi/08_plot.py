import matplotlib.pyplot as plt

# Read data
procs = []
times = []
with open("execution_times.txt", "r") as f:
    for line in f:
        p, t = line.split()
        procs.append(int(p))
        times.append(float(t))

# Plot
plt.figure(figsize=(6,4))
plt.plot(procs, times, marker='o')
plt.title("Number of Processes vs Execution Time")
plt.xlabel("Number of Processes")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.show()
