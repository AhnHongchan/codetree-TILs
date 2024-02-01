num = int(input())
for i in range(1, (2*num)+1):
    if i % 2 == 1:
        for j in range(int((i+1)/2)):
            print('*', end =" ")
    
    else:
        for j in range(int(num+1-(i/2))):
            print('*', end=" ")
    
    print()