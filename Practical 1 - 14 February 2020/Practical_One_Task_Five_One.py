# Practical Task 5.1
# Code By Ephraim Pillar

currentTimeStr = input("What is the time now in hours?")
numberOfHoursToWaitStr = input("How many hours to wait for the alarm?")

currentTimeInt = int(currentTimeStr)
numberOfHoursToWaitInt = int(numberOfHoursToWaitStr)

alarmTime = ((currentTimeInt + numberOfHoursToWaitInt) % 24)

print("The time on the clock when the alarm goes off will be: " , alarmTime)

