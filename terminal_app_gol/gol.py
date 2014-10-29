import os
import time

class Game():
  def __init__(self, current): # array of arrays with 0/1
    self.current = current
    self.next = [[0 for x in xrange(5)] for x in xrange(5)]

  def find_neighbors(self, x, y): # needs to be refactored
    neighbors = []
    bound = len(self.current)
    for i in range((x-1), (x+2)):
        for j in range((y-1), (y+2)):
          if i >= 0 and j >= 0 and i < bound and j < bound and not [i,j] == [x,y]:
            neighbors.append(self.current[i][j])

    return neighbors

  def stage_progress(self, x, y):
    test = sum(self.find_neighbors(x, y))
    if self.current[x][y] == 1:
      if test < 2:
        self.next[x][y] = 0
      if test == 2 or test == 3:
        self.next[x][y] = 1
      if test > 3:
        self.next[x][y] = 0
    else:
      if test == 3:
        self.next[x][y] = 1

  def play(self, test=0):
    self.display()
    for x, v in enumerate(self.current):
      for y, v in enumerate(self.current):
        self.stage_progress(x,y)
    self.current = self.next
    self.next = [[0 for x in xrange(5)] for x in xrange(5)]
    time.sleep(3)
    if test == 0:
      self.play()

  def display(self):
     for x in self.current:
        print x


# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
