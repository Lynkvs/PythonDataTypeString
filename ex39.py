def reverse_string(input_string):
    return input_string[::-1] # Użyj cięcia z [::-1], aby odwrócić ciąg wejściowy

# Test:
input_string = "Samolot"
# Wywołanie funkcji reverse_string w celu odwrócenia ciągu wejściowego
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
