def find_longest_word(words):
    if not words:
        return None, 0
    longest_word = '' # Inicjalizacja zmiennej do przechowywania najdłuższego słowa
    longest_length = 0 # Inicjalizacja zmiennej do przechowywania długości najdłuższego słowa
    for word in words: # przejdz przez każde słowo
        if len(word) > longest_length:
            # Sprawdza, czy długość bieżącego słowa jest większa niż długość najdłuższego
            # słowa znalezionego do tej pory.
            longest_word = word # Zaktualizuj najdłuższe słowo
            longest_length = len(word)
            # Zwraca najdłuższe słowo i jego długość
    return longest_word, longest_length
# Test
words_list = ["apple", "banana", "orange", "strawberry", "kiwi"]
longest_word, length = find_longest_word(words_list)
print("Longest word:", longest_word)
print("Length of longest word:", length)
