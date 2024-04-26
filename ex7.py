def not_poor(str1):
    snot=str1.find('not')
    # znalezienie indexu not
    spoor=str1.find('poor')
    #znalezienie indexu poor
    if spoor>snot and snot>0 and spoor>0:
        # Sprawdza, czy w ciągu występują  'not' i 'poor'
        # i czy 'not' pojawia się przed 'poor' + czy  oba są poprzedzone jakimiś znakami
        str1=str1.replace(str1[snot:(spoor+4)], 'good')
        ## Zastąp „not poor” (włącznie) słowem „good”.
        return str1
    else:
        return str1

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
