def count_multiples(data_list):
    
    # Define the divisors we are checking against
    divisors = range(1, 10)
    
    # Use a dictionary to store the results
    multiples_count = {}
    
    # Iterate through each divisor
    for d in divisors:
        count = 0
        # Check every number in the input list
        for num in data_list:
            # If the number is a multiple of the divisor (remainder is 0)
            if num % d == 0:
                count += 1
        
        # Store the total count for the current divisor
        multiples_count[d] = count
        
    return multiples_count

# Input provided in the problem
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Get the result
result = count_multiples(input_list)

# Print the output
print(f"Input: {input_list}")
print(f"Output: {result}")
