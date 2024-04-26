def add_ing_or_ly(string):
    # sprawdzenie czy długość stringu jest mniejsza niż 3
    if len(string) < 3:
        return string
    # sprawdzenie czy string kończy się 'ing'
    elif string.endswith('ing'):
        # jeśli tak dodaj ly
        return string + 'ly'
    else:
        # w innym wypadku dodaj ing na końcu
        return string + 'ing'
# Test
test_strings = ['play', 'playing', 'run']
for test_string in test_strings:
    result = add_ing_or_ly(test_string)
    print(f"Original String: '{test_string}', Result: '{result}'")
