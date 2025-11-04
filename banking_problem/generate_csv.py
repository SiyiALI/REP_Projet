import csv

import banking_algorithm

factors = []
for precision in [30, 50, 80]:
    for method in ["iterative", "closed_form"]:
        for terms in [50, 100, 200, 500]:
            for n in [10, 20, 50, 100]:
                factors.append({"precision": precision, "method": method, "terms": terms, "n": n})

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