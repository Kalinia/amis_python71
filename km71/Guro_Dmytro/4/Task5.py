print("Searching similar numbers")
print("Enter first")
while True :
    try:
        n1 = int(input())
        break
    except ValueError:
      print("Please enter number")
print("Enter second nuumber")
while True:
    try:
        n2 = int(input())
        break
    except ValueError:
        print("Please enter number")
print("Enter third number")
while True:
    try:
        n3 = int(input())
        break
    except ValueError:
        print("Please enter number")
if n1 == n2 and n2 == n3:
   print("3")
elif n1 == n2 or n2 == n3 or n3 == n1:
   print("2")
else:
    print("0")

input()