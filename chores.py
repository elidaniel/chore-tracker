#!/usr/bin/python


import time
import sys

class Day:
  Mon = 0
  Tue = 1
  Wed = 2
  Thu = 3
  Fri = 4
  Sat = 5
  Sun = 7
  Names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  

People = ['Eli', 'Ezra', 'Zech']

#------------------------------------------------------------------------------

ChoreList = []

def AddChore(PersonList, Chore):
  print "Adding {0} for {1}".format(Chore, str(ChoreList))
  
  for person in PersonList:
    if person in People:
       break
  else:
    person = 'NONE'
    
  ChoreList.append((person, Chore))

#------------------------------------------------------------------------------

# Get today to use as the default date input
today = time.strftime('%Y-%m-%d')

print
print 'Enter the date you want the chores for in YYYY-MM-DD format, okay?'
print 'If you enter nothing, then we will use today, which is', today, '.'
print
dateinput = raw_input('Enter date or nothing: ').strip()

if dateinput == '':
  dateinput = today

try:
  workdate = time.strptime(dateinput, '%Y-%m-%d')
except ValueError as e:
  print 
  print e
  print
  sys.exit()

print
print 'You entered', time.strftime('%A, %B %d, %Y', workdate)


# --------------------------------------------------------------------------------
# Figure out when it is...

dayofyear = workdate.tm_yday
dayofweek = workdate.tm_wday

print
print "The day of the year is:", dayofyear
print "The day of the week is:", Day.Names[dayofweek]

mod3 = dayofyear % 3

print dayofyear, "divided by 3 has a remainder of", mod3, "."
print


# --------------------------------------------------------------------------------
# This is the cat chore

print "----- Kitty Cat Chore -----"

print 'Ezra: do the water chore'
print 'Ezra: feed and water the cat'

if dayofweek in (Day.Thu, Day.Sun):
  print 'Ezra: dump litter; clear litter; add new litter; clean around litter'
else:
  print 'Ezra: scoop the litter; sweep if needed, double check!'

print

# --------------------------------------------------------------------------------
# This is the sweeping chore

if dayofweek != Day.Sun: 
  print 'Ezra: sweep the living room and dining room'
  print 'Ezra: scrub the living room and dining room as needed'
  print 'Eli : sweep the kitchen'
  print 'Eli : scrub the kitchen'
  print 'Zech: clean the  living room and dining room; but only if needed'
  print 'Zech: do the trash chore'
else:   
  print 'Ezra: sweep the living room and dining room, but only if needed'
  print 'Ezra: scrub the living room and dining room, but only if needed'
  print 'Eli : sweep the kitchen, but only if needed'
  print 'Eli : scrub the kitchen, but only if needed'

# --------------------------------------------------------------------------------
# This is the Bathroom chore

print "----- Bathroom Chore -----"

if dayofweek != Day.Sun: 
  print 'Eli : do the bathroom'
else:   
  print 'Eli : clean the bathroom sink and toliet, but only if needed'
   
print 

# --------------------------------------------------------------------------------
# This is the dishes chore

print '----- Dishes Chore -----'

print 'Eli : Do the dishes; do them again as needed all day'

print

# --------------------------------------------------------------------------------
# This is the Laundry Chore
if mod3 == 0:
  print 'Ezra: do the Light Laundry'
  print 'Ezra: do the Bath Towels Laundry'
elif mod3 == 1:
  print 'Ezra: do the Pants Laundry'
  print 'Ezra: do the Rags Laundry'
elif mod3 == 2:
  print 'Ezra: do the Dark Laundry'
  print 'Ezra: do the Kitchen Towels Laundry'

# --------------------------------------------------------------------------------
print




