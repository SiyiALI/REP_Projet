from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("."))

template = env.get_template("property_template.py.jinja")


experiments = [
    {"repetitions": 1000, "operation1": "(x + y) + z", "operation2": "x + (y + z)"},
    {"repetitions": 10000, "operation1": "x + y", "operation2": "y + x"},
    {"repetitions": 5000, "operation1": "(x * y) * z", "operation2": "x * (y * z)"}
]

for i, factors in enumerate(experiments):
    code = template.render(factors)
    filename = f"generated_property_check_{i}.py"
    with open(filename, "w") as f:
        f.write(code)
    print(f"generated files: {filename}")
    #os.system(f"python3 {filename}")

