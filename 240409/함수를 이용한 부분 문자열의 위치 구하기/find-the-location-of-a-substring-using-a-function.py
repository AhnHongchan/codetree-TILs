pro = input()
goal = input()

for i in range(len(pro)-len(goal)+1):
    if pro[i:i+len(goal)] == goal:
        print(i)
else:
    print(-1)