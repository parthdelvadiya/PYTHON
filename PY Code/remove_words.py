def remove_stopwords(text):
    stopwords = {"is", "the", "a"}
    return [word for word in text.split() if word not in stopwords]

print(remove_stopwords("ai is the future"))
['ai', 'future']