def count_characters(string):
    #przechowywania częstotliwości znaków
    char_frequency = {}
    #Iteracja przez każdy znak w ciągu znaków
    for char in string:
     #Jeśli znak znajduje się już w słowniku, zwiększ jego liczbę
        if char in char_frequency:
            char_frequency[char] += 1
      #Jeśli znaku nie ma w słowniku, należy go dodać z liczbą 1
        else:
            char_frequency[char] = 1
    return char_frequency
# Test
sample_string = 'lotams.com'
result = count_characters(sample_string)
print("Sample String:", sample_string)
print("Expected Result:", result)
