def removee(list1):
    # list1=list(set(list1))
    result=[]
    for i in list1:
        if i not in result:
            result.append(i)
    
    return result

print(removee([5,8,8,89,8]))