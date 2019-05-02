#! /usr/bin/env python3

# Calculates and re-constructs the first line of a number pyramid given an outside diagonal

# Creates a list with binomials (n, k) for each integer k <= n
# Follows the formula: (n, k) = (n, k-1) * (n + 1 - k)/k
def calculate_coefficients(n):
    coefficients = [1]
    if n > 0:
        for i in range(n):
            fraction = (n + 1 - (i + 1))/(i + 1)
            next_coeff = int(fraction * coefficients[i])
            coefficients.append(next_coeff)
    return coefficients

def main():
    input_array = input('Enger diagonal numbers, top to bottom: ')
    diag_number = [int(i) for i in input_array.split()]
    pyramid_size = len(diag_number)
    output = []

    # The term n_k at index k in the first row can be found by the following:
    # sum(-1^i * Pascal_row_k(i) * n_i for all i <= k)
    for i in range(pyramid_size):
        coefficients = calculate_coefficients(i)
        numbers = [((-1) ** (i-j)) * coefficients[j] * diag_number[j] for j in range(i+1)]
        next_value = sum(numbers)
        output.append(next_value)
		
    print(output)

if __name__ == '__main__':
    main()
