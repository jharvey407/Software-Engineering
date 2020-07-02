def cCipher(message, offset):
    while type(message) == str:
        output = ''
        for char in message:
            output += chr(ord(char)+offset)
        return(output)
    else:
        return('The input is not a string.')

print(cCipher('abc', 1))
print(cCipher('123', 3))
print(cCipher(44, 3))
print(cCipher('143Hg!)>#', 2))
print(cCipher("Here's 2 U MRS Robinson", 1))
