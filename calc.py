
import sys


num = raw_input('Enter the first number: ')
opr = raw_input('Enter operator + - / *: ')
den = raw_input('enter the other number: ')


try:
  num = int(num)
except ValueError:
  print "You did not enter a good first number"
  sys.exit()  
  
try:
  den = int(den)
except ValueError:
  print "You did not enter a good other number"
  sys.exit()  


if opr == '+':
  ans = num + den
  
elif opr == '-':
  ans = num - den

elif opr == '/':
  ans = num / den

elif opr == '*':
  ans = num * den

else:
  print "You did not enter a good operator."
  sys.exit()


print
print "The answer is: ", ans
print
