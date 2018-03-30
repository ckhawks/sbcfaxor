import binascii
import collections
import operator

def cmp(a, b):
    return ((a > b) - (a < b))

def readfile(filename):
    with open(filename, "r") as fp:
        message = binascii.unhexlify(fp.readline().strip())
    return message

message = readfile("file.txt")

matches = {}

dummytext = """Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn't listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way. On her way she met a copy. The copy warned the Little Blind Text, that where it came from it would have been rewritten a thousand times and everything that was left from its origin would be the word "and" and the Little Blind Text should turn around and return to its own, safe country. But nothing the copy said could convince her and so it didn't take long until a few insidious Copy Writers ambushed her, made her drunk with Longe and Parole and dragged her into their agency, where they abused her for their projects again and again. And if she hasn't been rewritten, then they are still using her.Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn't listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline"""
adummyt = collections.Counter(dummytext.lower())
ENGLISH = sorted(adummyt.items(), key=lambda i: i[1], reverse=True)
ENGLISH7 = []
print(ENGLISH)
for i in range(7):
    ENGLISH7.append(ENGLISH[i][0])

print(ENGLISH7)

for b in range(255):
    plaintext = ""
    for c in message:
        plaintext += chr(c ^ b)
    #print(plaintext)
    analysistext = collections.Counter(plaintext.lower())

    analSort = sorted(analysistext.items(), key=lambda i: i[1], reverse=True)
    analSort7 = []
    for i in range(7):
        analSort7.append(analSort[i][0])
    print(analSort7)

    count = 0
    for i in range(7):
        if analSort7[i] in ENGLISH7:
            count = count + 1
    matches[b] = count

print(matches)
matchesSorted = sorted(matches.items(), key=lambda x: x[1], reverse=True)
print(matchesSorted)

plaintext = ""
for c in message:
    plaintext += chr(c ^ matchesSorted[0][0])
print(plaintext)
