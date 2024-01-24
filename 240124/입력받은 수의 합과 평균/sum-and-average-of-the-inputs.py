num = int(input())
sum = 0
for i in range(num):
    a = int(input())
    sum += a

avg = round(sum/num, 1)
print(sum, avg)