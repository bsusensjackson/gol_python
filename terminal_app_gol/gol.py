import os
import time

class Game():
  def __init__(self, current): # array of arrays with 0/1
    self.current = current
    self.next = [[0 for x in current[0]] for x in current]

  def find_neighbors(self, x, y): # needs to be refactored
    neighbors = []
    for i in range((x-1), (x+2)):
        for j in range((y-1), (y+2)):
          if i >= 0 and j >= 0 and i < len(self.current) and j < len(self.current[0]) and not [i,j] == [x,y]:
            neighbors.append(self.current[i][j])

    return neighbors

  def stage_progress(self, x, y):
    test = sum(self.find_neighbors(x, y))
    if self.current[x][y] == 1:
      if test < 2:
        self.next[x][y] = 0
      elif test == 2 or test == 3:
        self.next[x][y] = 1
      elif test > 3:
        self.next[x][y] = 0
    else:
      if test == 3:
        self.next[x][y] = 1

  def play(self, test=0):
    os.system("clear")
    self.display()
    for x, v in enumerate(self.current):
      for y, v in enumerate(self.current[0]):
        self.stage_progress(x,y)
    self.current = self.next
    
    self.next = [[0 for length in self.current[0]] for length in self.current] 
    time.sleep(0.5)
    if test == 0:
      self.play()

  def display(self):
     for x in self.current:
        for y in x: 
          if y == 0:
            print " ",
          elif y == 1:
            print unichr(0x2588),
        print

results = []
with open('actual_glider.txt') as inputfile:
    for line in inputfile:
        line = list(line)
        if line[-1] == '\n':
          line.pop()
        line = map(lambda x: int(x), line)
        results.append(line)

game = Game(results)
print len(results[0])
game.play()

