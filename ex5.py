def chars_mix_up(y,z):
    new_y= z[:2]+y[2:]
    # Utwórz nowy ciąg dla y z pierwszymi dwoma znakami z z i resztą z y
    new_z= y[:2]+z[2:]
    # Utwórz nowy ciąg znaków dla z z pierwszymi dwoma znakami z y i resztą z z
    return new_y+new_z
print(chars_mix_up('pow', 'lof'))


