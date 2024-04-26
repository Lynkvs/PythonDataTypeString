def strip_characters(input_string, characters_to_strip):
    # Inicjalizacja pustego łańcucha do przechowywania usuniętych znaków
    stripped_string = ""
    # Iteracja przez każdy znak w ciągu wejściowym
    for char in input_string:
        # Sprawdź, czy znak nie znajduje się w zestawie characters_to_stri
        if char not in characters_to_strip:
            # Jeśli nie znajduje się w characters_to_strip, dodaje znak do stripped_string
            stripped_string += char
    return stripped_string

# Test
input_string = "Dawno temu !"
characters_to_strip = ",!"
stripped_string = strip_characters(input_string, characters_to_strip)
print("Original string:", input_string)
print("Stripped string:", stripped_string)
