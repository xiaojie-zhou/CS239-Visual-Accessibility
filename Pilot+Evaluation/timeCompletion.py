import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scienceplots

plt.style.use(['science', 'grid', 'no-latex'])
completion_times = [
    [20,29,23],
    [27,21,20],
    [20,29,23],
    [39,17,34],
    [25,22,21],
    [13,19,12],
    [28,20,22],
    [23,25,20],
    [25,27,23],
    [36,22,23],
]

completion_times = np.array(completion_times)


# Participant labels
participants = [f'P{i+1}' for i in range(10)]
# Assign colors for each participant
# Use the "Blues" colormap with different saturation levels
blues_cmap = cm.get_cmap("Blues", 12)  # 10 different shades of blue
colors = [blues_cmap((i+2) / 10 + 0.2) for i in range(10)]  # Adjust lightness by scaling

plt.figure(figsize=(5, 3))

# Scatter Plot
for i in range(10):  # Iterate through participants
    plt.scatter([participants[i]] * 3, completion_times[i, :], color=colors[i], alpha=0.5, s=50)

# Compute and plot mean completion time
mean_completion_time = np.mean(completion_times, axis=1)
plt.plot(participants, mean_completion_time, marker='^', linestyle='-', color='orange', label='Mean Completion Time', linewidth=2, markersize=10)

# Labels and title
plt.xlabel('Participants')
plt.ylabel('Completion Time (Seconds)')
plt.title('Task Completion Time for Each Participant')
plt.legend()
plt.grid(axis='x')
plt.tight_layout()
plt.savefig('timeCompletion.png', dpi=500)
plt.show()