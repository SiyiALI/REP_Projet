from decimal import Decimal, getcontext
import math

getcontext().prec = 50

def compute_e_decimal(terms=100):
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

# Parameters
method = "iterative"
n = 50
terms = 100

if method == "iterative":
    e_val = compute_e_decimal(terms)
    result = iterative_process(e_val, n)
else:
    e_val = compute_e_decimal(terms)
    result = closed_form(e_val, n)

print(f"Precision = 50, Terms = 100, Method = iterative, n = 50")
print(f"Final result ≈ {result}")
