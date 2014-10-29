from gol import *

g = Game([[0,0,0,0,0],
          [0,0,0,0,0],
          [0,1,1,1,0],
          [0,0,0,0,0],
          [0,0,0,0,0]])

def test_find_neighbors():
  assert g.find_neighbors(0,0) == [0,0,0]

def test_play():
  g.play(1)
  assert g.current == [[0,0,0,0,0],
                       [0,0,1,0,0],
                       [0,0,1,0,0],
                       [0,0,1,0,0],
                       [0,0,0,0,0]]
