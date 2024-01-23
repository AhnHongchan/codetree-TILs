a, b= map(int, input().split())
i = 0
if a < b:
    for i in range(b-a+1):
        print(b-i, end = " ")
else:
    for j in range(a-b+1):
        print(a-j, end = " ")