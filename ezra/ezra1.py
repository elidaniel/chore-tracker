from turtle import *

bgcolor('black')
color('white')


fill(True)

for i in range(8):
  forward(100)
  left(45)

fill(False)

color('red')

penup()

goto(0,100)

write('STOP', font=('arial', 80, 'bold'))


  
exitonclick()
