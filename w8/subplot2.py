import matplotlib.pyplot as plt

fig = plt.figure()
#ax = fig.add_subplot(2, 3, 1)
ax = fig.add_subplot(2, 3, 2)
ax = fig.add_subplot(2, 3, 3)
ax = fig.add_subplot(2, 3, 4)
ax = fig.add_subplot(2, 3, 5)

plt.savefig("subplot2.png")
plt.show()