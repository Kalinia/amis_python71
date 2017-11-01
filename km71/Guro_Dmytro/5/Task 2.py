while True:
    a = input('Enter a list of numbers: ').split()
    kol = 0
    for i in a:
        for b in a:
            if i == b:
                kol += 1
        kol -= 1
 print(int(count/2))
