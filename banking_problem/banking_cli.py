import argparse

import banking_algorithm

parser = argparse.ArgumentParser()
parser.add_argument('--method', choices=["iterative", "closed_form"], type=str, required=True)
parser.add_argument('--precision', type=int, required=True)
parser.add_argument('--terms', type=int, required=True)
parser.add_argument('--n', type=int, required=True)

args = parser.parse_args()
method = args.method
precision = args.precision
terms = args.terms
n = args.n

result = banking_algorithm.banking(precision, method, terms, n)

print(f"Precision = {precision}, Terms = {terms}, Method = {method}, n = {n}")
print(f"Final result ≈ {result}")

