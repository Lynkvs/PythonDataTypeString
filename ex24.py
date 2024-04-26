def starts_with(string, characters):
    return string.startswith(characters)

# Test
input_string = "Hello, world!" #zdefiniowanie stringu
specified_characters = "Hello" #zdefiniowanie specjalnych znaków
## Sprawdza, czy ciąg wejściowy zaczyna się od określonych znaków.
if starts_with(input_string, specified_characters):
    print(f"The string '{input_string}' starts with '{specified_characters}'.")
else:
    print(f"The string '{input_string}' does not start with '{specified_characters}'.")
