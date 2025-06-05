from sympy import Rational
from sympy.ntheory import continued_fraction_convergents
from math import isqrt

def is_perfect_square(n):
    x = isqrt(n)
    return x * x == n

def wiener_attack(e, n):
    for k_d in continued_fraction_convergents(Rational(e, n)):
        if k_d.q == 0:
            continue
        d = k_d.q
        k = k_d.p

        # Compute phi(n) = (ed - 1) / k
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k

        # Try solving x^2 - (n - phi + 1)x + n = 0
        a = 1
        b = -(n - phi + 1)
        c = n
        disc = b * b - 4 * a * c

        if disc >= 0 and is_perfect_square(disc):
            return d  # private exponent found

    return None
