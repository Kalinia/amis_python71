seq = [1,2,2,3,4,5,6,7,-8,100]

def secMax(lis):
    lis.remove(min(lis))
    if len(lis) == 2:
        return int(min(lis))
    else:
        return(secMax(lis))

print(secMax(seq))

