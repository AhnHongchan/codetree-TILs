a = 0
b = 0 
for i in range(10):
    num = int(input())
    if num % 3 == 0:
        a += 1
    if num % 5 == 0:
        b += 1

print(a, b)