import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

x = range(0, 10, 1)
y = range(0, 20, 2)

axes[0,0].plot(x, y)
axes[0,0].set_xlabel('Time')
axes[0,0].set_xlim(2, 8)
axes[0,0].set_ylabel('QA')
axes[0,0].set_ylim(-3, 16)

plt.tight_layout()

plt.savefig("subplot4.png")
plt.show()