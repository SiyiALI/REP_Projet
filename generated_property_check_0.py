import random
import csv

t = 0

def check_property():
    global t
    for i in range(1000):
        x = random.random()
        y = random.random()
        z = random.random()
        if not ((x + y) + z) == (x + (y + z)):
            t += 1

check_property()

result_value = t / 1000

with open("results_associativity.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([1000, "(x + y) + z", "x + (y + z)", result_value])