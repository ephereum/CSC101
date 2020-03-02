# Practical Task 5.2
# Code By Ephraim Pillar

startDayNumberStr = input("What is the starting day number?")
lengthOfStayStr = input("What is the length of stay?")

startDayNumberInt = int(startDayNumberStr)
lengthOfStayInt = int(lengthOfStayStr)

returnDayNumber = ((startDayNumberInt + lengthOfStayInt) % 7)

print("The number of day of the week you will return on is" , returnDayNumber)