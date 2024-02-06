T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    mul = 1
    for i in range(a, b+1):
        mul *= i
    
    print(mul)