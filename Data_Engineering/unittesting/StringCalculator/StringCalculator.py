def string_calculator(input_str):
    # Split the input string into a list of different bits
    different_bits = input_str.split()

    # get that first number in the calculation
    final_output = int(different_bits[0])

    # Iterate over the remaining tokens and perform the calculations in the correct order
    for i in range(1, len(different_bits), 2):
        operator = different_bits[i]
        operand = int(different_bits[i + 1])
        if operator == '+':
            final_output += operand
        elif operator == '-':
            final_output -= operand
        elif operator == '*':
            final_output *= operand
        elif operator == '/':
            final_output /= operand

    # Return the final "final_output"
    return final_output


string_calculator('3*4')
