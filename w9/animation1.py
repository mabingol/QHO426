import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
  pass

fig, ax = plt.subplots()

some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100, repeat = False)