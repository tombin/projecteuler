def alphaList():
    return [x for x in list(map(chr, range(97, 123)))]

def _cycle(key, cipherLen):
    newkey = []
    counter = 0
    while len(newkey) < cipherLen:
        newkey.append(key[counter])
        if counter == len(key) - 1:
            counter = 0
        else:
            counter += 1
    return newkey

def decrypt(cipher, key):
    commonWords = ["the", "be", "to", "of", "and"]
    decrypted = []
    xorValues = zip(cipher, key)
    for values in xorValues:
        decrypted.append(chr(int(values[0]) ^ ord(values[1])))
    decrypted = ''.join(decrypted)
    if all(word in decrypted for word in commonWords):
        print decrypted
        print "=" * 80
        return decrypted
         
def asciiSum(string):
    total = 0
    for char in string:
        total += ord(char)
    print total 

with open("cipher.txt", "r") as fd:
    cipherText = fd.read()

cipherText = cipherText.strip('\n').split(',')

for a in alphaList():
    for b in alphaList():
        for c in alphaList():
            key = _cycle(a + b + c, len(cipherText))
            decryptedText = decrypt(cipherText, key)
            if decryptedText:
                asciiSum(decryptedText) 
                

