s = "one two three four"
print(s.split(" ", 2))

['one', 'two', 'three four']
# 👉 Only splits 2 times

s = "a-b-c-d"
print(s.rsplit("-", 1))
['a-b-c', 'd']

s = "hello   world"
print(s.split())
['hello', 'world']

print(s.split(" "))
['hello', '', '', 'world']

s = "hello\nworld\nai"
print(s.splitlines())   
['hello', 'world', 'ai']

s = "hello"
print(list(s))
['h', 'e', 'l', 'l', 'o']

words = ['ai', 'is', 'cool']
print(" ".join(words))
# ai is cool

s = "  hello   world  "
print(" ".join(s.split()))
# print(" ".join(s.strip().split()))
# hello world

s="  heeellloooo   worrdss  "

# Reverse words
rev = " ".join(s.split()[::-1])
print(rev)
# worrdss heeellloooo