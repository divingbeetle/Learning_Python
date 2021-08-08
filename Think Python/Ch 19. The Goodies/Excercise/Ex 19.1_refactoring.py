"""

*** EX 19.1 ***
    Rewrite the function w/ nested conditional expressions
"""


def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """
    return 1 if k == 0 else (0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1))
