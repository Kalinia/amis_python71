print("Enter first number")
while True:
    try:
        x1=int(input())
        break
    except:
        print("Please enter number")
print("Enter second number")     
while True:
    try:
        y1=int(input())
        break
    except:
        print("Please enter number")
print("Entar third number")     
while True:
    try:
        x2=int(input())
        break
    except:
        print("Please enter number")
print("Enter fourth number")
while True:
    try:
        y2=int(input())
        break
    except:
        print("Please enter number")
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
