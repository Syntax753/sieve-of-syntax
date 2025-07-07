import math

def calculate_binary_sum(number_to_process: int) -> list:
    """
    Iterates over a binary number from right to left and calculates cumulative
    sums of modulo operations.

    For each '1' in the binary string (from right to left), the function
    calculates the corresponding power of 2 (1, 2, 4, 8...). It then takes
    this power of 2 and performs a modulo operation with each number
    in a predefined list. The result of each modulo operation is added to a
    running total for that number.

    Args:
        binary_string: A string representing a binary number.

    Returns:
        A dictionary where keys are numbers from the list and values are the
        cumulative sums of the modulo operations.
    """

    numbers_to_check = set()
    numbers_to_check.add(2)
    numbers_to_check.add(3)
    sums = {}
    divisors = [1, number_to_process]
    step = 0
    found = False
    while not found:
        binary_string = bin(number_to_process)[2:]
        print(f"Binary {binary_string}")
        
        print(numbers_to_check)
        # This will represent powers of 2 (1, 2, 4, 8...)
        idx = 1
        # We iterate from right to left by reversing the string.
        for digit_char in reversed(binary_string):
            # First, check if the digit is '1'.
            if digit_char == '1':
                # If it is, update the sums for each number in our list.
                for num in numbers_to_check:
                    # Initialize the key for the sum if it's not already present
                    if num not in sums:
                        sums[num] = 0
                    # Add the modulo result to the sum for the current number
                    sums[num] += idx % num
            # Double the index for the next position (power of 2).
            idx *= 2
        
        print(sums)

        # has_div = False
        # for i in sums:
        #     if sums[i] % i == 0:
        #         number_to_process = number_to_process // i
        #         print(f"Divisible by {i}. New number {number_to_process}")
        #         divisors.append(i)
        #         if number_to_process == 1:
        #             return divisors
        #         has_div = True

        # if has_div:

        #     numbers_to_check = set()
        #     numbers_to_check.add(2)
        #     numbers_to_check.add(3)
        #     sums = {}
        #     continue


        candidates = set()
        newNumbers = set()
        matches = {}

        # cnt = 0
        offs = []
        for next in sums:
            print(f"next {next}")
            
            offs.append((next,sums[next] % next))

            
            # for x in range(1, 5):
            #     candidate = (next*x + sums[next] % next)
            #     print(f"candidate {candidate}") 
            #     if candidate > math.sqrt(number_to_process):
            #         break

            #     if candidate > number_to_process:
            #         break
            #     if candidate %2 == 0:
            #         continue
            #     if candidate not in sums:
            #         newNumbers.add(candidate)
            #         cnt += 1
            #         print(f"found {candidate}")
            #         break
            #     else:
            #         print("already processed")

        disagree = True

        while disagree:
            
            step += 1
            print(f"step {step}")

            disagree = False
            off_tuple = offs[0]
            next_val = off_tuple[0]
            offset = off_tuple[1]
            print(f"Accessed tuple: next={next_val}, offset={offset}")

            val = next_val*step+offset

            # for off in offs[1:]:
            #     v_val = off[0]
            #     v_offset = off[1]
            #     print(f"Accessed tuplee: next={v_val}, offset={v_offset}")

            #     if (v_val+v_offset) % val == 0:
            #         newNumbers.add(val)
            #         disagree = False
            #         print(f"Matches {val}")                        


                # if val not in matches:
                #     matches[val] = 1
                # else:
                #     matches[val] += 1

                # if matches[val] == len(offs):
                #     disagree = False
                #     print(f"Matched {val}")
                #     newNumbers.add(val)

            # if not disagree:
            #     newNumbers.add(val)
            #     print(f"Matches {val}")

            # if val < math.sqrt(number_to_process):
            #     disagree = True                
            
        disagree = False
        print (newNumbers)

        if number_to_process == 1:
            Found = True

        Found = True
        # if cnt == 0:
        #     found = True

        numbers_to_check = newNumbers

    divisors.append(number_to_process)
    return divisors

# --- Demonstration ---
number_to_process = 1223
print(f"Processing the number: {number_to_process}")
divisors = calculate_binary_sum(number_to_process)


print("The divisors are:")
print(divisors)

