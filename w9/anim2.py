import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
  global ax
  ax.plot(range(range), range(frame))

squares_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100)
plt.show()