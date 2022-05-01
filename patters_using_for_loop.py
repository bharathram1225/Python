n = int(input("enter the number of rows: "))


for i in range(1,n):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print("\n \n")
    
        

for i in range(1,n):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

print("\n \n")


for i in range(1,n):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

print("\n \n")


for i in range(1,n):
    for j in range(1,i+1):
        print(n-i,end=" ")
    print()

print("\n \n")

for i  in range(1,n):
    for  j in range(1, i+1):
        print(n-j, end=" ")
    print()

print("\n \n")


for i  in range(0,n):
    for  j in range(i,-1,-1):
        print(n-j, end=" ")
    print()

print("\n \n")
print("\n differnt shape \n")

for i in range(n):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\n different patten of the same number system")
    
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()


print("\n 2. one or the next one")

for i in range(n):
    for j in range(i+1,0,-1):
        print(j, end=" ")
    print()
    


print("\n different patten of the same number system")


for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print(j, end=" ")
    print()



print("\n 3. one or the next one")

for i in range(n):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("\n different patten of the same number system")

for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
print("\n to print the pattern in the triangle share ")

for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()    
    

    
