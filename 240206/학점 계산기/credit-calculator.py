num = int(input())
grade = list(map(float, input().split()))

sum_val = 0
for i in range(len(grade)):
    sum_val += grade[i]

avg = sum_val / num
print(f'{avg:.1f}')
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')