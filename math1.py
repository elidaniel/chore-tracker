

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

