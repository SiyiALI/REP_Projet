from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("."))

template = env.get_template("banking_template.py.jinja")

# Différentes combinaisons de facteurs
factors = [
    {"precision": 30, "terms": 50, "method": "iterative", "n": 50},
    {"precision": 50, "terms": 100, "method": "iterative", "n": 50},
    {"precision": 80, "terms": 200, "method": "closed_form", "n": 50}
]

for i, f in enumerate(factors):
    filename = f"generated_banking_{i}.py"
    code = template.render(**f)
    with open(filename, "w") as out:
        out.write(code)
    print(f"Generated: {filename}")
    os.system(f"python3 {filename}")

