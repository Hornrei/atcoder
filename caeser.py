enc = 'fdhvdu'

key = 3

plain = ''

for char in list(enc):
    ascii = ord(char)
    num = ascii - 97
    num = (num - key) % 26
    ascii = num + 97
    plain += chr(ascii)

print(plain)