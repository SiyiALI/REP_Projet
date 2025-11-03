
import random

t = 0

def check_property():
    global t
    for i in range(10000):
        x = random.random()
        y = random.random()
        z = random.random()
        if not (x + y) == (y + x):
            t += 1

check_property()

with open("result.txt", "w") as f:
    f.write(f"Violation rate: {t}/10000")
