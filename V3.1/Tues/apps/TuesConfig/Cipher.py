# a = input(' -> ')
b = ''
c = ''


def encrypt(input):
    pc = 0
    encodedInput = ''
    for i in input:
        encodedInput += chr((ord(i) + 107 + pc - 32) % 95 + 32)
        pc = (ord(i) + 107 + pc) % 95

    return encodedInput


def decrypt(input):
    pc = 0
    reversedInput = ''
    for i in input:
        dc = (ord(i) - 107 - pc + 95 - 32) % 95
        reversedInput += chr(dc + 32)
        pc = ord(i)
    return reversedInput


print(encrypt('asd'))
print(decrypt(encrypt('asd')))

print('\n', b, '\n')
print(c)