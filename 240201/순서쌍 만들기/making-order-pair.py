num = int(input())

for i in range(num,0,-1):
    for j in range(num,0,-1):
        print(f"({i},{j})", end=" ")
    print()