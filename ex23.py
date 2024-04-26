def remove_newline(text):
    return text.replace("\n", "")
# użycie replace do zamiany newline na pusty znak
# Test
text_with_newline = "Dawno temu za\ngórami za lasami.\n"
text_without_newline = remove_newline(text_with_newline)
print("Original text:")
print(text_with_newline)
print("Text after removing newlines:")
print(text_without_newline)
