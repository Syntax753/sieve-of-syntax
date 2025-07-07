# sieve-of-syntax

    Finds the prime factors of a number using a custom modulo-based algorithm.

    This function uses an iterative approach to find factors. It calculates
    the modulo of powers of 2 against a list of candidate divisors to find
    congruences. It uses these congruences to generate new, more likely
    candidate divisors in each iteration, eventually converging on the
    actual factors of the number.
