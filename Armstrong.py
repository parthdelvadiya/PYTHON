def Armstrong(n):
    length=len(str(n))
    total_sum=0
    for i in str(n):
        total_sum=total_sum+(int(i)**length)
        
    return total_sum==n

print(Armstrong(845))