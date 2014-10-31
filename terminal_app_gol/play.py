from gol import *
import sys

def preface(file, folder='patterns/'):
  return folder + file

options = {"Gosper": preface('gosper_glider_gun.txt'),
           "Glider": preface('glider.txt'),
           "Rand": 0 }

def play():
    if sys.argv[1] in options.keys():
      game = Game(options[sys.argv[1]], 1)
      game.play() 
    else:
      print "We don't have that pattern... yet."

play()