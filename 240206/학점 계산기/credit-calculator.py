num = int(input())
grade = list(map(int, input().split()))

sum_val = 0
for i in range(len(grade)):
    sum_val += grade[i]

avg = sum_val / num
if avg >= 4.0:
    print(f'{avg:.1f} Perfect')
elif avg >= 3.0:
    print(f'{avg:.1f} Good')
else:
    print(f'{avg:.1f} Poor')