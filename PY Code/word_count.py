from collections import Counter

text = "ai is the future ai is powerful"
words = text.split()
result=Counter(words)

print(result)

# Counter({'ai': 2, 'is': 2, 'the': 1, 'future': 1, 'powerful': 1})