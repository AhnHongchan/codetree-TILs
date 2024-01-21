num = int(input())
if num % 2 == 1:
    num += 3
    
if num % 3 == 0:
    num = num // 3
print(num)