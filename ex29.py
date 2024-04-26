def set_first_line_indentation(text, indentation):
    lines = text.split('\n')  # podziel tekst na nowe linie
    if lines:  # sprawdza czy są jakieś linie w tekście
        lines[0] = indentation + lines[0].lstrip()  # Ustawienie wcięcia 1 linii
    return '\n'.join(lines)  # połączenie linii

# Test:
original_text = """samolot
    samochód
    rower"""
indentation = "\t"  # Example: użycie znaku tabulacji do wcięcia
text_with_changed_indentation = set_first_line_indentation(original_text, indentation)
print(text_with_changed_indentation)
