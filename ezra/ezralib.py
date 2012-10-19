
from turtle import *


def triangle(size):
  forward(size)
  left(120)
  forward(size)
  left(120)
  forward(size)
  left(120)


def square(size):
  forward(size)
  left(90)
  forward(size)
  left(90)
  forward(size)
  left(90)
  forward(size)
  left(90)
  

def nuclear(size):
  for i in range(6):
    if i % 2 == 0:
      fill(True)
    
    left(60)
    triangle(size)

    if i % 2 == 0:
      fill(False)

 
