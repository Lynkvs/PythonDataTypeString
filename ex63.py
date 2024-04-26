def remove_leading_zeros(ip_address):
    # Podzielenie adresu IP na oktety
    octets = ip_address.split('.')
    # Usunięcie pierwszych 0 z oktetu
    stripped_octets = [str(int(octet)) for octet in octets]
    # Połączenie oktetów z powrotem
    stripped_ip_address = '.'.join(stripped_octets)
    return stripped_ip_address
# Test
ip_address = "192.168.001.01"
stripped_ip_address = remove_leading_zeros(ip_address)
print("Original IP address:", ip_address)
print("Stripped IP address:", stripped_ip_address)
