import random, csv, os

REPS = 5000
OP1  = "(x * y) * z"
OP2  = "x * (y * z)"
DTYPE = "decimal50"
DIST  = "wide"
SEED  = 0

def gen_value(rng):
    if DIST == "uniform01":
        return rng.random()
    if DIST == "uniform_signed":
        return rng.uniform(-1.0, 1.0)
    if DIST == "wide":
        e = rng.randint(-300, 300)
        return rng.uniform(-1.0, 1.0) * (10.0 ** e)
    raise ValueError("unknown dist")

def cast(x):
    if DTYPE == "float64":
        return float(x)
    if DTYPE == "float32":
        import numpy as np
        return np.float32(x).item()
    if DTYPE.startswith("decimal"):
        from decimal import Decimal, localcontext, getcontext
        prec = int(DTYPE.replace("decimal",""))
        getcontext().prec = prec
        return Decimal(str(x))
    raise ValueError("unknown dtype")

t = 0
rng = random.Random(SEED)
for _ in range(REPS):
    x = cast(gen_value(rng))
    y = cast(gen_value(rng))
    z = cast(gen_value(rng))
    left  = eval(OP1)  
    right = eval(OP2)  
    if not (left == right):
        t += 1

result_value = t / REPS

with open("results_associativity.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([REPS, OP1, OP2, DTYPE, DIST, SEED, f"{result_value:.6f}"])