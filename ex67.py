def remove_consecutive_duplicates(input_string):
    # Initializacja stringu do przechowywania wyniku
    result = ""
    # Iteracja przez każdy znak w ciągu wejściowym
    for i in range(len(input_string)):
        # Dodanie bieżącego znaku do wyniku, jeśli różni się on od poprzedniego znaku.
        if i == 0 or input_string[i] != input_string[i - 1]:
            result += input_string[i]
    return result
# Test:
input_string = "aaabbbbcccdddeeefffg"
result = remove_consecutive_duplicates(input_string)
print("Original string:", input_string)
print("String with consecutive duplicates removed:", result)
