grade = list(map(float, input().split()))

sum = 0
for i in range(len(grade)):
    sum += grade[i]

avg = sum / len(grade)
print(f'{avg:.1f}')