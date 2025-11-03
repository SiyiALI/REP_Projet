import subprocess

operations = [
    (30, 50, "iterative", 50),
    (50, 100, "iterative", 50),
    (80, 200, "closed_form", 50),
]

for (precision, terms, method, n) in operations:
    subprocess.run(["python3", "banking_cli.py", "--precision", str(precision), "--terms", str(terms), "--method", str(method), "--n", str(n)])