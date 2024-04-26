def print_numbers(numbers):
    for number in numbers: #powtórz po każdej liczbie
        #wypisanie liczb z 2 miejscami po przecinku
        print("{:.2f}".format(number))

# Example usage:
numbers = [3.14159, 2.71828, 1.41421, 0.57721]
print_numbers(numbers)
