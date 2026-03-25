def missing(list1):
    length=len(list1)+1
    return length*(length+1)//2 - sum(list1)

print(missing([1,2,3,4,5,6,7,8,10,9,11,12,13,15]))