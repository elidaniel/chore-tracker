

WIDTH = 80
HEIGHT = 30

GRID = [[' ' for y in range(HEIGHT)] for x in range(WIDTH)]



def point(x,y):
  GRID[x][y] = "O"


def draw():
  print
  print "+" + "-"*WIDTH + "+"
  for y in range(HEIGHT):
    print "|" + "".join((GRID[x][y] for x in range(WIDTH))) + "|" 

  print "+" + "-"*WIDTH + "+"
  print

