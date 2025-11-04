import random, csv, os

def gen_value(rng, dist):
    if dist == "uniform01":
        return rng.random()
    if dist == "uniform_signed":
        return rng.uniform(-1.0, 1.0)
    if dist == "wide":
        e = rng.randint(-300, 300)
        return rng.uniform(-1.0, 1.0) * (10.0 ** e)
    raise ValueError("unknown dist")

def cast(x, dtype):
    if dtype == "float64":
        return float(x)
    if dtype == "float32":
        import numpy as np
        return np.float32(x).item()
    if dtype.startswith("decimal"):
        from decimal import Decimal, localcontext, getcontext
        prec = int(dtype.replace("decimal",""))
        getcontext().prec = prec
        return Decimal(str(x))
    raise ValueError("unknown dtype")

def eval_associativity(seed, reps, rng, op1, op2, dtype):
    t = 0
    rang = random.Random(seed)
    for _ in range(reps):
        x = cast(gen_value(rang, dist), dtype)
        y = cast(gen_value(rang, dist), dtype)
        z = cast(gen_value(rang, dist), dtype)
        left  = eval(op1)  
        right = eval(op2)  
        if not (left == right):
            t += 1

    return t / reps

experiments = []
for base in [
    {"repetitions": 1000,  "op1": "(x + y) + z", "op2": "x + (y + z)"},
    {"repetitions": 10000, "op1": "x + y",       "op2": "y + x"},
    {"repetitions": 5000,  "op1": "(x * y) * z", "op2": "x * (y * z)"},
]:
    for dtype in ["float64", "float32", "decimal50"]:
        for dist in ["uniform01", "uniform_signed", "wide"]:
            for seed in [0, 1]:
                for rng in ["uniform01", "uniform_signed", "wide"]:
                    experiments.append({**base, "dtype": dtype, "dist": dist, "seed": seed, "rng": rng})

with open("results_associativity.csv", "a", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["repetitions", "op1", "op2", "dtype", "dist", "seed", "rng", "result"])
    writer.writeheader()

    for experiment in experiments:
        reps = experiment["repetitions"]
        op1  = experiment["op1"]
        op2  = experiment["op2"]
        dtype = experiment["dtype"]
        dist  = experiment["dist"]
        seed = experiment["seed"]
        rng = experiment["rng"]

        result = eval_associativity(seed, reps, rng, op1, op2, dtype)

        writer.writerow(experiment | {"result": result})