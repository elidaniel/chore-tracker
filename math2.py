import random

###############################################################################
def makenumber(small, large):
  # Take the large number minus the small number and that is the gap
  gap = large - small

  # Make a random number from 0.000 to 1.000 and multiply it times the gap.
  # convert it to an integer so there are not 123.456 decimals
  rand = int(random.random() * gap) 
  
  # Take the random number and add it to the small number to give you the
  # correct range.
  num = rand + small
  
  # Return the number
  return num

###############################################################################
def makeproblem(ptype):
  
  #=========================================================================
  if ptype == 'add1':
    x = makenumber(0,10)
    y = makenumber(0,10)
    return "{0:3} + {1:3} = ____".format(x,y) 
  
  #=========================================================================
  elif ptype == 'sub1':
    x = makenumber(0,10)
    y = makenumber(0,10)
    if y > x:  #flip them if y is greater than x
      x,y = y,x 
    return "  {0:3}\n- {1:3}\n-----\n=    \n\n".format(x,y) 
  
  #=========================================================================
  elif ptype == 'sub:2-1':
    x = makenumber(10,100)
    y = makenumber(0,10)
    return "  {0:3}\n- {1:3}\n-----\n=    \n\n".format(x,y) 
  
  #=========================================================================
  else:
    raise ValueError("Bad value passed to makeproblem(): " + str(ptype)) 

###############################################################################
print "===================================================="
print

for i in range(8):
  print makeproblem('add1')

print
print "===================================================="
print

for i in range(8):
  print makeproblem('sub1')

print
print "===================================================="
print

for i in range(8):
  print makeproblem('sub:2-1') 