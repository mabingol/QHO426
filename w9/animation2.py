import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
  global ax
  ax.plot(range(frame), range(frame))

some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100)
plt.show()