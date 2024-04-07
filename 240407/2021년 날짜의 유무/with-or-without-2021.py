M, D = map(int, input().split())

long = [1,3,5,7,8,10,12]
short = [4,6,9,11]

result = 'No'
if M in long:
    if D <= 31:
        result = 'Yes'
elif M in short:
    if D <= 30:
        result = 'Yes'
elif M == 2:
    if D <= 28:
        result = 'Yes'

print(result)