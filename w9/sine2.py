import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

line = None

def animate(frame):
  global line
  x = np.arange(0, frame)
  y = np.sin(x * (np.pi / 180))
  line.set_data(x, y)

def run():
  global line
  fig, ax = plt.subplots()
  ax.set_xlim(0, 720)
  ax.set_ylim(-1, 1)
  line, = ax.plot([], [], linewidth = 3)
  sine_animation = animation.FuncAnimation( fig, animate, frames = 720, interval = 1)
  
  sine_animation.save('sin_graph.mp4', fps=15)
  plt.show()

run()