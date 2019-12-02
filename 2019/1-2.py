import math

input = open("input1-1.txt")

input = input.readlines()

def fuel_requirements(x):
    if x < 6:
        return 0
    else:
        x = math.floor(int(x)/3)-2
        return (x + fuel_requirements(x))

result = sum([fuel_requirements(int(x)) for x in input])

print(result)

