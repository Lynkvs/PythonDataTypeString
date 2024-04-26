def display_number_with_comma(number):
    # Funkcja formatu
    formatted_number = "{:,}".format(number)
    print("Using format function:", formatted_number)

    # Użycie f-string
    formatted_number_fstring = f"{number:,}"
    print("Using f-string:", formatted_number_fstring)

# Test
number = 1000000
display_number_with_comma(number)
