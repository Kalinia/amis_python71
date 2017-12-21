def Rev(lis,n = 0):
    if n != len(lis):
        print(lis[len(lis) - 1 - n],end = " ")
        n += 1
        return Rev(lis,n)
    return ''
    
Rev([-3, -2, -1, 0, 1, 2, 3])
