from decimal import Decimal, getcontext
import math

def compute_e_decimal(terms):
    e = Decimal(0)
    fact = Decimal(1)
    for k in range(0, terms):
        if k > 0:
            fact *= Decimal(k)
        e += Decimal(1) / fact
    return e

def iterative_process(A0, n):
    A = Decimal(A0)
    for k in range(1, n+1):
        A = (A - Decimal(1)) * Decimal(k)
    return A - Decimal(1)

def closed_form(A0, n):
    fact = Decimal(1)
    partial = Decimal(0)
    for j in range(0, n):
        if j > 0:
            fact *= Decimal(j)
        partial += Decimal(1) / fact
    fact_n = fact * Decimal(n) if n > 0 else Decimal(1)
    A_n = fact_n * (Decimal(A0) - partial)
    return A_n - Decimal(1)

parser = argparse.ArgumentParser()
parser.add_argument('--method', type=str, required=True)
parser.add_argument('--precision', type=int, required=True)
parser.add_argument('--terms', type=int, required=True)
parser.add_argument('--n', type=int, required=True)

args = parser.parse_args()
method = args.method
precision = args.precision
terms = args.terms
n = args.n

getcontext().prec = precision

if method == "iterative":
    e_val = compute_e_decimal(terms)
    result = iterative_process(e_val, n)
else:
    e_val = compute_e_decimal(terms)
    result = closed_form(e_val, n)

print(f"Precision = {precision}, Terms = {terms}, Method = {method}, n = {n}")
print(f"Final result ≈ {result}")

