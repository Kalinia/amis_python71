print("Searching minimum of 3 numbers ")
print("Number 1")
while True :
    try:
        n1 = int(input())
        break
    except:
        print("Please enter number")
print("Number 2")
while True :
    try:
        n2 = int(input())
        break
    except:
        print("Please enter number")
print("Number 3")
while True:
     try:
         n3 = int(input())
         break
     except:
         print("Please enter number")

                
minimum = n1

if n2 < minimum:
          minimum = n2
if n3 < minimum:
          minimum = n3
print("Min is ", minimum)
