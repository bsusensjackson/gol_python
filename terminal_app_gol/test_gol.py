from gol import * 
c = Cell(1, 1, True)

def test_create_cell():
  assert isinstance(c, Cell) == True 

def test_cell_attributes():
  assert hasattr(c, 'x') == True
  assert hasattr(c, 'y') == True
  assert hasattr(c, 'alive') == True
