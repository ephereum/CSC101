# Coded by Ephraim Pillar G20P0425

base = int(input("Enter the base:"))
exponent = int(input("Enter the exponent:"))

answer = 1

for exp in range(exponent):
    answer = answer * base
    
print("The answer is:",answer)