def Long(string1):
    words=string1.split()
    max_len=0
    max_word=""
    for i in words:
        if len(i)>max_len:
            max_len=len(i)
            max_word=i
            
    # return max(words,key=len)
    return max_word,max_len
    
print(Long("Okauad aoakoka ajjajai"))