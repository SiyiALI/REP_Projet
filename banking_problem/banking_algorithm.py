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

def banking(precision, method, terms, n):
    getcontext().prec = precision

    e_val = compute_e_decimal(terms)
    
    if method == "iterative":
        return iterative_process(e_val, n) - 1 # for retrieval fee
    else:
        return closed_form(e_val, n) - 1 # for retrieval fee

if __name__ == "__main__":
    n = 50
    e = compute_e_decimal(terms=200)

    after_n_iterations = iterative_process(e, n)

    print("Method: iterative")
    print(f"Initial {e=}")
    print(f"After {n=} years (before retrieval fee): A_n ≈ {after_n_iterations}")
    print(f"After paying final €1 retrieval fee: final ≈ {after_n_iterations - 1}")