# Practical Task 5.3
# Code By Ephraim Pillar

P = 10000
n = 12
r = 0.08

t = int(input("Please enter the number of years:"))

principalAmountCalculation = P * ( (1 + (r/n)) ** (n*t) )

print("The final amount after" , t , "years:" , "R", principalAmountCalculation)