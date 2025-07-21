def power(base, exponent):
    powers = [1]  # Initialize with the base case

    # Precompute powers of the base up to the exponent
    for _ in range(exponent.bit_length() - 1):
        powers.append(powers[-1] * powers[-1])

    result = 1
    mask = 1 << (exponent.bit_length() - 1)

    # Multiply relevant precomputed powers to get the final result
    for power in powers[::-1]:
        result *= power if (exponent & mask) else 1
        mask >>= 1

    return result
 
def fibbonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result