import sys
import random
from gol import *

def preface(file, folder='terminal_app_gol/patterns/'):
  return folder + file

options = { "gosper": preface('gosper_glider_gun.txt'),
            "glider": preface('glider.txt') }

def play():
    u_input = sys.argv[1].lower()
    if u_input in options.keys():
      game = Game(options[u_input], 1)
      game.play() 
    elif u_input == "rand":
      x_bound = random.randint(15, 35)
      y_bound = random.randint(15, 35)
      game = Game(
                   [[random.randint(0,1) for x in xrange(x_bound)] 
                     for x in xrange(y_bound)]
                  )
      game.play()

    else:
      print "We don't have that pattern... yet."

play()