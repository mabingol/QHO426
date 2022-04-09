import matplotlib.pyplot as plt

xpoints = [1, 2, 6, 8]
ypoints = [3, 8, 1, 10]

#plt.plot(xpoints, ypoints)
#plt.plot(xpoints, ypoints, "o")
#plt.plot(ypoints, 'o:r')

#plt.plot(ypoints, marker = 'o', ms = 20)
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
#plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.plot(ypoints, marker = 'v', ms = 20, mec = 'r', mfc = 'hotpink')

plt.show()