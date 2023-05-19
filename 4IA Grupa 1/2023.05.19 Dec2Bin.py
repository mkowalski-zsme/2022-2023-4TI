def dec2bin(liczba:int) -> str:
    ret = ''
    while liczba != 0:
        ret = str(liczba%2) + ret
        liczba //= 2

    return ret




def bin2dec(text: str) -> int:
    ret = 0
    w = 1
    for i in text[::-1]:
        if i == '1':
            ret += w
            w *= 2
        elif i == '0':
            w *= 2

    return ret




print(dec2bin(85))

print(bin2dec('1111 1101'))


p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def palindrom(string):
    if string == string[::-1]: return True
    else: return False


print(palindrom('CC 00 CC'))