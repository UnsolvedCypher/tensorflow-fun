import random
import math
import string


#fifty fifty
letters = 'abcdefghijklmnopqrstuvwxyz'
f = open('fifty-fifty.csv', 'w')
for yes in range(1000):
    pal = round(random.random())
    word = ''
    if pal == 0:
        for i in range(4):
            word = word + random.choice(letters)
    else:
        ch1 = random.choice(letters)
        ch2 = random.choice(letters)
        word = word + ch1
        word = word + ch2
        word = word + ch2
        word = word + ch1
    word = word + (", true" if pal else ", false")
    print(word)
    f.write(word+'\n')
f.close

#ninety ten
letters = 'abcdefghijklmnopqrstuvwxyz'
f = open('ninety-ten.csv', 'w')
for yes in range(1000):
    pal = random.random()
    word = ''
    if pal > 0.9:
        for i in range(4):
            word = word + random.choice(letters)
    else:
        ch1 = random.choice(letters)
        ch2 = random.choice(letters)
        word = word + ch1
        word = word + ch2
        word = word + ch2
        word = word + ch1
    word = word + (", true" if pal else ", false")
    print(word)
    f.write(word+'\n')
f.close

#ten ninety
letters = 'abcdefghijklmnopqrstuvwxyz'
f = open('ten-ninety.csv', 'w')
for yes in range(1000):
    pal = random.random()
    word = ''
    if pal > 0.1:
        for i in range(4):
            word = word + random.choice(letters)
    else:
        ch1 = random.choice(letters)
        ch2 = random.choice(letters)
        word = word + ch1
        word = word + ch2
        word = word + ch2
        word = word + ch1
    word = word + (", true" if pal else ", false")
    print(word)
    f.write(word+'\n')
f.close