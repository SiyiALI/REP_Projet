import subprocess

operations = [
    (0.0, 1.0, 1000),
    (0.0, 1.0, 10000),
    (-1.0, 1.0, 1000),
    (-1.0, 1.0, 10000),
    (-1000, 1000, 1000),
    (-1000, 1000, 10000),
]

for (min, max, steps) in operations:
    subprocess.run(["python3", "main_cli.py", "--min", str(min), "--max", str(max), "--steps", str(steps)])