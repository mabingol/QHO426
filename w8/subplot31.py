import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

a2022 = range(0, 10, 1)
qa2022 = range(0, 20, 2)

i = [1,2,3,4,5,6,7,8,9,10]
j = [t**2 for t in i]

axes[0,0].plot(a2022, qa2022)
axes[1,1].plot(i, j)



plt.savefig("subplot31.png")
plt.show()