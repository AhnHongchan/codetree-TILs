num = int(input())
for i in range(num):
    for j in range(num-i):
        print('*', end ="")

    for k in range(2*i):
        print(" ", end = "")
    
    for j in range(num-i):
        print('*', end ="")
    
    print()