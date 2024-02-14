import time
import os
from grid import Grid

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

grid = Grid(70, 280)

currentGneration = 0
while True:
  cls()
  grid.draw()
  time.sleep(0.1)
  grid.generateNewGeneration()
  currentGneration+= 1

  if currentGneration >= 40:
    currentGneration = 0
    del(grid)
    grid = Grid(70, 280)