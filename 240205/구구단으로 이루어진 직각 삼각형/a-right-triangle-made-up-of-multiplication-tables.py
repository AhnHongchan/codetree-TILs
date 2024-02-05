num = int(input())

for i in range(1, num + 1):
    for j in range(1, num - i + 2):
        if j != num - i + 1:
            print(f"{i} * {j} = {i * j}", end=' / ')
        else:
            print(f"{i} * {j} = {i * j}")