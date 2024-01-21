num = int(input())
if num % 2 == 0:
    num //= 2
if num % 2 == 1:
    num = (num+1) // 2
print(num)