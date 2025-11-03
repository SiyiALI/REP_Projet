import csv

import banking_algorithm

factors = [
    {"precision": 30, "terms": 50, "method": "iterative", "n": 50},
    {"precision": 50, "terms": 100, "method": "iterative", "n": 50},
    {"precision": 80, "terms": 200, "method": "closed_form", "n": 50}
]

with open("results_banking.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["precision", "terms", "method", "n", "result"])

    writer.writeheader()
    for factor_set in factors:
        result = banking_algorithm.banking(
            factor_set["precision"],
            factor_set["method"],
            factor_set["terms"],
            factor_set["n"]
        )

        writer.writerow(factor_set | {"result": result})