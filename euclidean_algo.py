import random as rand
def euclidean_gcd(a, b):
    steps = []
    while b != 0:
        q = a // b
        r = a % b
        steps.append(f"{a} = {b} * {q} + {r}")
        a, b = b, r
    steps.append(f"GCD is {a}")
    return a, steps


a = rand.randrange(0,500)
b = rand.randrange(0,500)
gcd, process = euclidean_gcd(a, b)

for step in process:
    print(step)
