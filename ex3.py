def get_first_and_last_two_chars(input_str):
    if len(input_str) < 2:
     #Sprawdza, czy długość ciągu wejściowego jest mniejsza niż 2.
        return ''
    # jesli tak zwraca pusta wartosc string
    else:
        return input_str[:2] + input_str[-2:]
# Jeśli długość ciągu wejściowego wynosi 2 lub więcej, łączy pierwsze dwa znaki
 # z dwoma ostatnimi znakami i zwróci wynik
# Test cases
sample_strings = ['k9resource', 'k9', ' k']
for string in sample_strings:
    result = get_first_and_last_two_chars(string)
    print(f"Sample String: '{string}', Expected Result: '{result}'")
