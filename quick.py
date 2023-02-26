from operator import floordiv, mod

def divide_exact(n, d):
    """Return the quotient and the remainder of dividing N by D.

    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n,d)
