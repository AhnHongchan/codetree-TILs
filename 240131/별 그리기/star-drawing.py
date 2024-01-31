# 변수 선언 및 입력
n = int(input())

# Step 1:
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end="")
    for _ in range(2 * i - 1):
        print("*", end="")
    for _ in range(n - i):
        print(" ", end="")
    print()

# Step 2:
for i in range(n - 1, 0, -1):
    for _ in range(n - i):
        print(" ", end="")
    for _ in range(2 * i - 1):
        print("*", end="")
    for _ in range(n - i):
        print(" ", end="")
    print()