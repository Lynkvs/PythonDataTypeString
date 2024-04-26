def find_smallest_and_largest_words(input_string):
    words = input_string.split()
    # Inicjalizacja zmiennych do przechowywania najmniejszego i największego słowa
    smallest_word = None
    largest_word = None
    # Iteruj przez każde słowo na liście słów
    for word in words:
        # Jeśli smallest_word nie zostało jeszcze przypisane lub bieżące słowo jest mniejsze niż smallest_word
        if smallest_word is None or len(word) < len(smallest_word):
            smallest_word = word
        # Jeśli largest_word nie zostało jeszcze przypisane lub bieżące słowo jest większe niż largest_word
        if largest_word is None or len(word) > len(largest_word):
            largest_word = word
    return smallest_word, largest_word
# Test
input_string = "Python is an amazing language"
smallest, largest = find_smallest_and_largest_words(input_string)
print("Smallest word:", smallest)
print("Largest word:", largest)
