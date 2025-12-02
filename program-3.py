def generate_odd_series_by_input(a: int):
    
    if not isinstance(a, int) or a <= 0:
        print(f"Input a = {a} (Invalid Input, must be a positive integer)")
        return "Error: Input must be a positive integer."

    # 1. Determine the number of terms (N) to generate.
    if a % 2 != 0:
        # If 'a' is odd, N is 'a'.
        num_of_terms = a
    else:
        # If 'a' is even, N is 'a - 1'.
        num_of_terms = a - 1

    # 2. Generate the first N odd positive integers (1, 3, 5, ...).
    output_series = []
    
    # The nth odd positive integer is given by the formula: 2*n + 1
    # Since range starts at 0, we iterate from i = 0 up to num_of_terms - 1.
    for i in range(num_of_terms):
        odd_number = 2 * i + 1
        output_series.append(odd_number)

    # Print the output in the requested format
    print(f"Input a = {a}, then output: {', '.join(map(str, output_series))}")
    return output_series

# --- Examples based on the problem statement ---
print("--- Problem Examples ---")
generate_odd_series_by_input(1)
generate_odd_series_by_input(2)
generate_odd_series_by_input(3)
generate_odd_series_by_input(4)
generate_odd_series_by_input(5)
generate_odd_series_by_input(6)
generate_odd_series_by_input(7)
