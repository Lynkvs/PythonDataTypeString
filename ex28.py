def add_prefix_to_lines(text, prefix):
    # Podzielenie tekstu na linie za pomocą '\n'
    lines = text.split('\n')
    # Dodanie prefiksu do każdej linii przy użyciu list kompresii
    prefixed_lines = [prefix + line for line in lines]
    return '\n'.join(prefixed_lines) # Połączenie linii z powrotem za pomocą '\n'

# Test:
original_text = """orzech
banan
brzoskwinia"""
prefix = "Testowo: "
prefixed_text = add_prefix_to_lines(original_text, prefix)
print(prefixed_text)
