import random as rand
#formula
"""240x+46y=gcd(240,46)"""
def extended_euclidean(a, b):
    old_r, r = a, b
    old_s, s = 1, 0  
    old_t, t = 0, 1  

    steps = []

    while r != 0:
        q = old_r // r
        steps.append(f"{old_r} = {q}*{r} + {old_r - q * r}")
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    steps.append(f"GCD = {old_r}, x = {old_s}, y = {old_t}")
    return old_r, old_s, old_t, steps

a = rand.randrange(0,500)
b = rand.randrange(0,500)

gcd, x, y, process = extended_euclidean(a, b)

for step in process:
    print(step)

print(f"\n{a}*({x}) + {b}*({y}) = {gcd}")
