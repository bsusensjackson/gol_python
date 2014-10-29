from gol import *

g = Game([[0,0,0],
          [1,1,1],
          [0,0,0]])

def test_find_neighbors():
  assert g.find_neighbors(1,1) == [0,0,0,1,1,0,0,0]
