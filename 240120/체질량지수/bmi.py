height, fat = map(int, input().split())
height_m = height / 100
BMI = int(fat / (height_m ** 2))
print(BMI)
if BMI >= 25:
    print('Obesity')