# Coded by Ephraim Pillar G20P0425

userInput = int(input("Calculate factorial for which number?: "))

def factorial(n):
    factorialAnswer = 1
    for x in range(n):
        factorialAnswer = factorialAnswer * (x + 1)
    return factorialAnswer

factorialAnswer = factorial(userInput)
print(factorialAnswer)    
