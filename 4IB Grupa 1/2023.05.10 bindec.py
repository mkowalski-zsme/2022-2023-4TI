def Dec2Bin(liczba):
    ret = ''
    while liczba > 0:        
        r = liczba % 2
        liczba = liczba // 2
        ret = str(r) + ret
    return ret


def Bin2Dec(text):
    ret = 0
    pot = 1
    for i in text[::-1]:
        if i == '1':
            ret += pot
        pot *= 2
    return ret

print(Dec2Bin(255))
print(Bin2Dec('10010110'))
print(Bin2Dec('11111111'))