import random


def generate_name():
    with open("texts/planets.txt", "r") as f:
        raw = f.read()
    planets = raw.split("\n")
    total_syllables = 0
    syllables = []
    for p in planets:
        lex = p.split("-")
        for l in lex:
            if l not in syllables:
                syllables.append(l)
    size = len(syllables) + 1
    freq = [[0] * size for i in range(size)]
    for p in planets:
        lex = p.split("-")
        i = 0
        while i < len(lex) - 1:
            freq[syllables.index(lex[i])][syllables.index(lex[i+1])] += 1
            i += 1
        freq[syllables.index(lex[len(lex) - 1])][size-1] += 1
    planet_name = ""
    suffixes = ["prime", str(random.randint(100,9999)),"B", str(random.randint(100,9999)),"alpha",str(random.randint(100,9999)),'proxima', str(random.randint(100,9999)),"IV", str(random.randint(100,9999)),"V", str(random.randint(100,9999)),"C", str(random.randint(100,9999)),"VI", str(random.randint(100,9999)),"VII", str(random.randint(100,9999)),"VIII", str(random.randint(100,9999)),"X", str(random.randint(100,9999)),"IX", str(random.randint(100,9999)),"D",str(random.randint(100,9999)),str(random.randint(100,9999)), str(random.randint(100,9999))]
    length = random.randint(2, 3)
    initial = random.randint(0, size - 2)
    while length > 0:
        while 1 not in freq[initial]:
            initial = random.randint(0, size - 2)
        planet_name += syllables[initial]
        initial = freq[initial].index(1)
        length -= 1
    suffix_index = random.randint(0, len(suffixes) - 1)
    planet_name += " "
    planet_name += suffixes[suffix_index]
    return planet_name



