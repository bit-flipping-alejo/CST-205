# CST 205 lab 15
# Ivan Alejandre
# Alejandro Caicedo

import calendar
import time
from datetime import date

def calendarFun():
  # birthday calendars
  ivanBday = [27, 9, 1988]
  alejoBday = [1, 1, 1987] # change date
  
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
  
  
