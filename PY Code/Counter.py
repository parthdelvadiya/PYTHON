from collections import Counter

s = "banana"
c = Counter(s)

print(c)
# {'b': 1, 'a': 3, 'n': 2}

c = Counter("banana")
print(c.most_common(1))
# [('a', 3)]

print(c.most_common(2))
# [('a', 3), ('n', 2)]
