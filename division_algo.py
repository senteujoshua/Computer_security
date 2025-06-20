import random as rand

def division_algorithm(a, b):
    q = a // b
    r = a % b
    return q, r

# Example
a = rand.randint(-50,-10)
b = rand.randint(0,10)

q, r = division_algorithm(a, b)
print(f"{a} = {b} * {q} + {r}")