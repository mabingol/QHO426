import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 3)
x = range(0, 10, 1)
y = range(0, 20, 2)


axes[0,0].plot(x, y)
axes[1,0].plot(x, y)
axes[2,1].plot(x, y)

plt.savefig("subplot3.png")
plt.show()