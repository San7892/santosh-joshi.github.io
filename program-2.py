def generate_odd_series(a: int):
    
    if a <= 0:
        return "Input must be a positive integer."

    output_series = []
    # We iterate 'a' times to get 'a' numbers in total
    for i in range(a):
        # The nth odd positive integer is given by the formula: 2*n + 1
        # Since 'i' starts at 0 (for the 1st number), the formula is: 2*i + 1
        odd_number = 2 * i + 1
        output_series.append(odd_number)

    # Print the output in the requested format (comma-separated string)
    print(f"Input a = {a}, then output: {', '.join(map(str, output_series))}")
    return output_series

# --- Examples ---
print("--- Examples ---")
generate_odd_series(1)
generate_odd_series(2)
generate_odd_series(3)
generate_odd_series(4)
generate_odd_series(7)
