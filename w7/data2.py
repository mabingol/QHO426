import matplotlib.pyplot as plt

xs = [1,2,3,4,5,6,7,8,9,10]
ys = [x**2 for x in xs]

plt.plot(xs, ys)
plt.show()