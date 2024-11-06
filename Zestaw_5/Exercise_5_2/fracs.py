from math import gcd  # fractions.gcd() is deprecated since Python 3.5


def verify_frac(frac):
    if len(frac) != 2:
        raise ValueError("Fraction must have exactly 2 elements")
    if frac[1] == 0:
        raise ValueError("Denominator cannot be zero")
    if type(frac[0]) != int or type(frac[1]) != int:
        raise ValueError("Both elements must be integers")


def simplify(frac):
    common_gcd = gcd(frac[0], frac[1])
    frac[0] = frac[0] // common_gcd
    frac[1] = frac[1] // common_gcd
    if frac[1] < 0:
        frac[0] = -frac[0]
        frac[1] = -frac[1]
    return frac


def add_frac(frac1, frac2):
    verify_frac(frac1)
    verify_frac(frac2)

    return simplify([frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]])


def sub_frac(frac1, frac2):
    verify_frac(frac1)
    verify_frac(frac2)

    return simplify([frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]])


def mul_frac(frac1, frac2):
    verify_frac(frac1)
    verify_frac(frac2)

    return simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):
    verify_frac(frac1)
    verify_frac(frac2)
    if frac2[0] == 0:
        raise ValueError("Denominator cannot be zero")

    return simplify([frac1[0] * frac2[1], frac1[1] * frac2[0]])


def is_positive(frac):
    verify_frac(frac)
    return True if frac[0] * frac[1] > 0 else False


def is_zero(frac):
    verify_frac(frac)
    return True if frac[0] == 0 else False


def cmp_frac(frac1, frac2):
    verify_frac(frac1)
    verify_frac(frac2)
    simplify(frac1)
    simplify(frac2)

    print(frac1)
    print(frac2)

    if frac1[0] * frac2[1] > frac2[0] * frac1[1]:
        return 1
    elif frac1[0] * frac2[1] < frac2[0] * frac1[1]:
        return -1
    else:
        return 0


def frac2float(frac):
    verify_frac(frac)
    return frac[0] / frac[1]
