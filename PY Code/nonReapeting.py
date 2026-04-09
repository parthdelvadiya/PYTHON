from collections import Counter

def first_unique(s):
    c = Counter(s)
    for ch in s:
        if c[ch] == 1:
            return ch

print(first_unique("aabbcde"))  # c