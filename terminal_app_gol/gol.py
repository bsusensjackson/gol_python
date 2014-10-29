class Game():
  def __init__(self, current): # array of arrays with 0/1
    self.current = current
    self.next = []

  def find_neighbors(self, x, y): # needs to be refactored
    return [self.current[x - 1][y - 1],
            self.current[x - 1][y],
            self.current[x - 1][y + 1],
            self.current[x][y - 1],
            self.current[x][y + 1],
            self.current[x + 1][y - 1],
            self.current[x + 1][y],
            self.current[x + 1][y + 1]]


# 5 x 5
# (1, 2), (2,2), (3,2)
# (2, 1), (2,2), (2,3)

# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
