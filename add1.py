import random
def getnumber():
   return int(random.random() * 10)

x = getnumber()
y = getnumber()
z = x + y

print "What is:  ", x, "+", y, "?"
print
print 
print "Answer:   ", x, "+", y, "=", z
=======================================================================================================================
pyton math.py
import random
def makenumber():
   return int(random.random() * 100)

def makeproblem():
   x = makenumber()
   y = makenumber()
   return "{0} + {1} = ____".format(x,y)

print "===================================================="
print
print makeproblem()
print