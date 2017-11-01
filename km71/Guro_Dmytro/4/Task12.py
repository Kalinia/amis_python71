while True:
    try:
        n = int(input("Enter num of width-squares"))
        break
    except:
        print("Please enter number")
while True:
    try:
        m = int(input("Enter num of length-squares"))
        break
    except:
        print("Please enter number")
print("Enter num of full squares after action")     
while True:
    try:
        k = int(input())
        break
    except:
        print("Please enter number")
        
if n * m - k == n or n * m - k == m and n * m > k and k > 1:
    print('YES')
elif (n * m - k ) % 2 == 0 and n * m > k and k > 1:
    print('YES')
else:
    print('NO')
