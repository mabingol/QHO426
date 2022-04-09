import matplotlib.pyplot as plt

labels = ('Jan', 'Feb', 'Mar', 'Apr','May')
sizes = [15, 30, 45, 90,450]

plt.pie(sizes, labels=labels)
plt.show()