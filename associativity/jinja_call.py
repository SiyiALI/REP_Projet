from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("."))

template = env.get_template("associativity_property_template.py.jinja")

experiments = []
for base in [
    {"repetitions": 1000,  "operation1": "(x + y) + z", "operation2": "x + (y + z)"},
    {"repetitions": 10000, "operation1": "x + y",       "operation2": "y + x"},
    {"repetitions": 5000,  "operation1": "(x * y) * z", "operation2": "x * (y * z)"},
]:
    for dtype in ["float64", "float32", "decimal50"]:
        for dist in ["uniform01", "uniform_signed", "wide"]:
            for seed in [0, 1]:
                experiments.append({**base, "dtype": dtype, "dist": dist, "seed": seed})


for i, factors in enumerate(experiments):
    code = template.render(factors)
    filename = f"generated_property_check_{i}.py"
    with open(filename, "w") as f:
        f.write(code)
    print(f"generated files: {filename}")

