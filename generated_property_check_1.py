import random
import csv

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

result_value = t / 10000

with open("results_associativity.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([10000, "x + y", "y + x", result_value])