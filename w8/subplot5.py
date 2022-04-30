
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, axs = plt.subplots(2, 2)

x = range(0, 10, 1)
y = range(0, 20, 2)

axs[0,0].plot(x, y)

axs[0,0].set_xlabel('X')
axs[0,0].set_xlim(-13, 21)

axs[0,0].set_ylabel('Y')
axs[0,0].set_ylim(-1, 31)

axs[0,0].tick_params(which='both', width = 2)
axs[0,0].tick_params(which='major', length = 8, color = 'g')
axs[0,0].tick_params(which='minor', length = 21, color = 'r')

axs[0,0].xaxis.set_minor_locator(MultipleLocator(1))
axs[0,0].yaxis.set_minor_locator(MultipleLocator(2))
axs[0,0].xaxis.set_major_locator(MultipleLocator(2))
axs[0,0].yaxis.set_major_locator(MultipleLocator(4))

plt.tight_layout()

plt.savefig("subplot5.png")
plt.show()