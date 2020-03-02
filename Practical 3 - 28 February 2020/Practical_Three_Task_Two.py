# Coded by Ephraim Pillar G20P0425

def hypotenuse():
    a = int(input("Input the value for one side: "))
    b = int(input("Input the value for ther other side: "))
    c = ((a**2)+(b**2))**0.5
    return c

print(hypotenuse())