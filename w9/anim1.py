import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
  print(f'Frame: {frame}')
  #print()

def run():
  fig, ax = plt.subplots()
  
  
  simple_animation = animation.FuncAnimation(fig, animate, frames = 15, interval = 100)
  plt.show()

run()