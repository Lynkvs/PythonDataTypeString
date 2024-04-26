def reverse_words(input_string):
    # Podziel ciąg wejściowy na słowa
    words = input_string.split()
    # Odwrócenie kolejności słów
    reversed_words = words[::-1]
    # Połączenie odwróconych słów z powrotem w ciąg znaków
    reversed_string = ' '.join(reversed_words)
    return reversed_string
# Test
input_string = "Latam samolotem boeing"
reversed_string = reverse_words(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
