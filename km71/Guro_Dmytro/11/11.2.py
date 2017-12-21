def Min(lis):

    if len(lis) != 1:
        if lis[0] >= lis[1]:
            return Min(lis[1:])
        else:
            del lis[1]
            return Min(lis)
    else:
        return lis[0]
    
p = [-3,2,0,-5]
temp = list(p) 
print(Min(temp))
