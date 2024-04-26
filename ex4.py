def change_first_char_occurrences(string):
    # Pobiera pierwszy znak z ciągu znaków
    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')
    # zastępuje wszystkie powtarzające się znaki(1 litera wyrazu) na $ pomijając znak na początku
    return modified_string

# Test
sample_string = 'restart'
result = change_first_char_occurrences(sample_string)
print("Sample String:", sample_string)
print("Expected Result:", result)
