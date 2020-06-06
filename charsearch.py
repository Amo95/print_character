# naive method 1

def charnum(word):
    word_dict = dict()

    for i in word:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
            
    char = input("Enter character: ")
    return f"{char}: {word_dict[char]}\n"

print("naive method 1")
print("=" * 15)
print(charnum(input("Enter word: ")))

# naive method 2

def char():
    word = input("Enter word: ")
    char = input("Enter a character: ")
    num = 0

    for i in word:
        if i == char:
            num += 1
    return f"{num} number of {char} in {word}"

print("naive method 2")
print("=" * 15)
print(char())


# count() method

def counts(word):
    char = input("Enter character: ")
    word = word.count(char)
    return f"{char}: {word}"

print(counts(input("Enter word: ")))


# collections.Counter()

from collections import Counter

word = input("Enter word: ")
count = Counter(word)
print(count[input("Enter character: ")])

# labda() + sum() + map()

def lam():
    word = input("Enter word: ")
    char = input("Enter character: ")
    word = sum(map(lambda x: 1 if char in x else 0, word))
    return word

print(lam())
