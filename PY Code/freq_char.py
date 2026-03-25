def count(st):
    freq={}
    max_len=0
    max_len_char=""
    for i in st:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1   
            
    for key,value in freq.items():
        if value>max_len:
            max_len=value
            max_len_char=key            
    return freq,max_len,max_len_char

print(count("Okay y   yyyayahdj"))