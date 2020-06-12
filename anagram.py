# Anagram

def anagram(fword, sword):
    fword = fword.lower()
    sword = sword.lower()
    return sorted(fword) == sorted(sword)

print(anagram("iceman", "cinema"))
