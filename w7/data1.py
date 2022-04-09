import matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

x2 = [0,2,4,6,8,10]
y2 = [10,14,12,60,3,45]

plt.xlabel("time")
plt.ylabel("price")

plt.title('Interesting Graph\nCheck it out')


plt.plot(x, y, label='January')
plt.plot(x2,y2, marker = 'o', ms = 3, mec = 'r', label='February')
#for a,b in zip(x2, y2): 
#    plt.text(a, b, str(b))
#plt.plot(x, y, "o")
#plt.step(x, y)
#plt.bar(x, y)

plt.legend()

plt.savefig("line.pdf")
plt.show()