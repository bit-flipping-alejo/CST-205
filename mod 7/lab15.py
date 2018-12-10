# CST 205 lab 15
# Ivan Alejandre
# Alejandro Caicedo

def play_craps():
  printNow(" - First Roll - ")
  point = roll_2dice()
  printNow("You rolled a: " + str(point))
  
  firstRollCheck = intant_winLose(point)
  
  if firstRollCheck == 0 or firstRollCheck == 1:
    return

  printNow( str(point) + " is the point")
  printNow(" - LETS PLAY CRAPS! - ")
  
  result = sim_craps(point)
  if result:
    printNow("!!! YOU WIN !!!!")
  else:
    printNow("!!! YOU LOSE !!!!")



#
# roll_2dice
#    rolls 2 dice
def roll_2dice():
  return roll_dice() + roll_dice()

#
# roll_dice
#    rolls 1 dice
def roll_dice():
  import random
  #default seeds with curr second
  random.seed()
  #below ensures if 2 close calls same number
  #is not returned 
  for i in range(0, random.randint(0,10)):
    random.randint(1,6)
  return random.randint(1,6)
  
#
# check initial roll
#  if 7/11 win (return 1), if 2/3/12 lose (return 0),
#  else returns 2  
def intant_winLose(firstRoll):
  if ((firstRoll == 7) or (firstRoll == 11)):
    printNow(" !!!  YOU WIN !!!")
    return 1  
  if ((firstRoll == 2) or (firstRoll == 3) or (firstRoll == 12)):
    printNow(" !!!  YOU LOSE !!!")
    return 0    
  return 2  

#
# sim_craps(point)
#    Takes in point int and simulates
#    rolls until you win (roll the point) 
#    or lose (roll a 7)
#    returns true if win, false if lose
def sim_craps(point):
  idx = 2
  while true:
    currRoll = roll_2dice()
    printNow("Roll #" + str(idx))
    idx = idx + 1
    printNow("You Rolled a: " + str(currRoll))
    if currRoll == 7:
      return false
    if currRoll == point:
      return true 


def calendarFun():
  import calendar
  import time
  from datetime import date
  # birthday calendars
  ivanBday = [27, 9, 1988]
  alejoBday = [3, 10, 1990] # change date
  
  print ("Ivan's birthday month:\n")
  ivanCalendar = calendar.TextCalendar(calendar.SUNDAY)
  ivanCalendar.prmonth(ivanBday[2], ivanBday[1])
  
  print ("\nAlejandro's birthday month:\n")
  alejoCalendar = calendar.TextCalendar(calendar.SUNDAY)
  alejoCalendar.prmonth(alejoBday[2], alejoBday[1])
  
  # countdown to bday
  currentDate = date.today()
  ivanBday = date(currentDate.year, 9, 27)
  alejoBday = date(currentDate.year, 7, 7) # change date
  
  if ivanBday < currentDate:
    ivanBday = ivanBday.replace(year=currentDate.year + 1)
    
  if alejoBday < currentDate:
    alejoBday = alejoBday.replace(year=currentDate.year + 1)
  
  timeToIvanBday = abs(ivanBday - currentDate)
  timeToAlejoBday = abs(alejoBday - currentDate)
  print "\nTime to Ivan's next birthday: ", timeToIvanBday.days
  print "\nTime to Alejandro's next birthday: ", timeToAlejoBday.days
  
  # independance date
  independance = calendar.TextCalendar(calendar.SUNDAY)
  day = calendar.weekday(1776, 7, 4)
  dayNames = calendar.day_name
  print("\nThe Declaration of Independance was signed on " + dayNames[day] + ", July 4th, 1776.")
  
  
