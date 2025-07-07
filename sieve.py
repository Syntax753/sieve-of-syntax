import math

def find_prime_factors(number_to_process: int) -> list:
    """
    Finds the prime factors of a number using a custom modulo-based algorithm.

    This function uses an iterative approach to find factors. It calculates
    the modulo of powers of 2 against a list of candidate divisors to find
    congruences. It uses these congruences to generate new, more likely
    candidate divisors in each iteration, eventually converging on the
    actual factors of the number.

    Args:
        number_to_process: The integer to be factorized.

    Returns:
        A list containing the prime factors of the input number.
    """
    original_number = number_to_process
    divisors = []

    # Handle the factor of 2 separately
    while number_to_process % 2 == 0:
        divisors.append(2)
        number_to_process //= 2

    # If the number is now 1, we are done.
    if number_to_process == 1:
        return divisors

    # Start with a base list of odd numbers to check.
    numbers_to_check = [3, 5]

    while number_to_process > 1:
        # If we run out of candidates, the remaining number is prime.
        if not numbers_to_check:
            divisors.append(number_to_process)
            break

        binary_string = bin(number_to_process)[2:]
        sums = {num: 0 for num in numbers_to_check}
        
        # This will represent powers of 2 (1, 2, 4, 8...)
        idx = 1
        # We iterate from right to left by reversing the string.
        for digit_char in reversed(binary_string):
            if digit_char == '1':
                for num in numbers_to_check:
                    sums[num] += idx % num
            idx *= 2
        
        has_divisor = False
        # Check if any of our current numbers are divisors
        for num in numbers_to_check:
            if sums[num] % num == 0:
                print(f"Found factor: {num}")
                divisors.append(num)
                while number_to_process % num == 0:
                    number_to_process //= num
                has_divisor = True
        
        # If we found a divisor, restart the process with the new number
        if has_divisor:
            numbers_to_check = [3, 5] # Reset candidates
            continue

        # --- Generate new candidates if no factors were found ---
        
        # Ensure we have at least two numbers to create candidate lists from
        if len(numbers_to_check) < 2:
             divisors.append(number_to_process) # The rest is prime
             break

        candidate_1 = []
        n1 = numbers_to_check[0]
        # The sum for n1 gives us the offset for its arithmetic progression
        offset1 = number_to_process % n1 # Simplified from sums[n1] % n1
        for x in range(1, int(math.sqrt(original_number))):
            candidate = n1 * x + offset1
            if candidate > 1 and candidate % 2 != 0: # Must be odd and > 1
                 candidate_1.append(candidate)

        candidate_2 = []
        n2 = numbers_to_check[1]
        offset2 = number_to_process % n2 # Simplified from sums[n2] % n2
        for x in range(1, int(math.sqrt(original_number))):
            candidate = n2 * x + offset2
            if candidate > 1 and candidate % 2 != 0:
                candidate_2.append(candidate)

        # The new numbers to check are the common elements of the two progressions
        numbers_to_check = sorted(list(set(candidate_1) & set(candidate_2)))

    return sorted(divisors)

# --- Demonstration ---
number_to_process = 23171
print(f"Processing the number: {number_to_process}")
factors = find_prime_factors(number_to_process)

print("\nThe prime factors are:")
print(factors)

# Verification
if factors:
    product = 1
    for f in factors:
        product *= f
    print(f"\nVerification: Product of factors is {product}")
    if product == 23171:
        print("Factorization is correct.")
    else:
        print("Factorization is incorrect.")


