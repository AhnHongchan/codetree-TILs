num = int(input())

for i in range(num):    
    for j in range(num-i-1):
        print(" ", end =" ")
    for k in range(i+1):
        print("@", end = " ")
    print()

for i in range(num-2,-1,-1):
    for j in range(i+1):
        print("@", end = " ")
    print()