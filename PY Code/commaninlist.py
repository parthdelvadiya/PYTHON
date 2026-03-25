list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
comman=[]

for i in list1:
    for j in list2:
        if i==j:
            comman.append(i)
            
print(comman)