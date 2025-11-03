from decimal import Decimal, getcontext

getcontext().prec = 120

def compute_e_decimal(terms=200):
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
    final = A - Decimal(1)
    return A, final

def closed_form(A0, n):
    fact = Decimal(1)
    partial = Decimal(0)
    for j in range(0, n):
        if j > 0:
            fact *= Decimal(j)
        partial += Decimal(1) / fact
    fact_n = fact * Decimal(n) if n > 0 else Decimal(1)
    A_n = fact_n * (Decimal(A0) - partial)
    final = A_n - Decimal(1)
    return A_n, final

n = 50
e_dec = compute_e_decimal(terms=200)

A_n_iter, final_iter = iterative_process(e_dec, n)
A_n_closed, final_closed = closed_form(e_dec, n)

print("Initial e =", e_dec)
print(f"After {n} years (before retrieval fee): A_n ≈ {A_n_iter}")
print(f"After paying final €1 retrieval fee: final ≈ {final_iter}")

