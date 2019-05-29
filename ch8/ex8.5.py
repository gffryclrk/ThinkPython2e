def rot(n):
    def encode(string):
        encoded_string = ''
        for c in string:
            if c.islower():
                encoded_string += chr(97 + ((ord(c) - 97 + n) % 26) )
            elif c.isupper():
                encoded_string += chr(65 + ((ord(c) - 65 + n) % 26) )
            else: 
                encoded_string += c

        return encoded_string
    return encode

encoder = rot(10)
print(encoder('zebra'))

decoder = rot(-10)
print(decoder(encoder('zebra')))

print(encoder('HeLlo this IS A meSSaGE'))
print(decoder(encoder('HeLlo this IS A meSSaGE')))
