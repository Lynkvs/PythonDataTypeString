def remove_nth_character(string, n):
    # Sprawdź, czy n jest prawidłowe (w zakresie długości łańcucha)
    if n < 0 or n >= len(string):
        print("Invalid index.")
        return string  # zwraca oryginalny ciąg, jeśli indeks jest nieprawidłowy
    new_string = string[:n] + string[n + 1:] #tworzy nowy ciag, wykluczająć n
    return new_string
# Test
input_string = "kosiarka"
index_to_remove = 3
result = remove_nth_character(input_string, index_to_remove)
print("Original string:", input_string)
print("String after removing character at index", index_to_remove, ":", result)
