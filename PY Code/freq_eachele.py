from collections import Counter # Recommended for efficiency

my_list = ['a', 'b', 'a', 'c', 'b', 'a']
frequency = Counter(my_list)
print(frequency) 


count_dict = {}
for item in my_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1