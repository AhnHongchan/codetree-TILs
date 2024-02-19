num = int(input())
sum_val = 0
for i in range(num):
    x = int(input())
    sum_val += x

y = str(sum_val)
y = y[1:] + y[0]
print(y)