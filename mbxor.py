import binascii
import collections
import operator

def cmp(a, b):
    return ((a > b) - (a < b))

def readFile(filename):
    with open(filename, "r") as fp:
        message = fp.readline().strip()
    return message

def readFileHex(filename):
    return binascii.unhexlify(readFile(filename))

debug = False
def dprint(string):
    if(debug):
        print(string)

def singlebyteXOR(sbkey, message):
    plaintext = ""
    for c in message:
        plaintext += chr(c ^ sbkey)
    return plaintext

def singleByteFreq(input, englishSample):
    matches = {}

    englishCounter = collections.Counter(englishSample.lower())
    ENGLISH = sorted(englishCounter.items(), key=lambda i: i[1], reverse=True)
    ENGLISH7 = []
    dprint(ENGLISH)
    for i in range(7):
        ENGLISH7.append(ENGLISH[i][0])

    dprint(ENGLISH7)

    for b in range(255):
        plaintext = singlebyteXOR(b, input)
        dprint(plaintext)

        analysistext = collections.Counter(plaintext.lower())
        analSort = sorted(analysistext.items(), key=lambda i: i[1], reverse=True)
        analSort7 = []
        for i in range(7):
            analSort7.append(analSort[i][0])
        dprint(analSort7)

        count = 0
        for i in range(7):
            if analSort7[i] in ENGLISH7:
                count = count + 1
        matches[b] = count

    dprint(matches)
    matchesSorted = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    dprint(matchesSorted)

    output = singlebyteXOR(matchesSorted[0][0], input)
    print(output)

inputtext = readFileHex("file.txt")
englishSample = readFile("english.txt")
singleByteFreq(inputtext, englishSample)
