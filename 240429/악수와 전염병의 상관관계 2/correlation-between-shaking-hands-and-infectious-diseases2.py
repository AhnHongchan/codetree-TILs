N, K, P, T = map(int, input().split())
people = [0] * (N+1)
people[P] = 1

shake = [0] * (N+1)
arr = []
for i in range(T):
    t,x,y = map(int, input().split())
    arr.append([t,x,y])

arr.sort(key=lambda x : x[0])

for i in range(len(arr)):
    if people[arr[i][1]] == 1 and people[arr[i][2]] == 0:
        if shake[arr[i][1]] < K:
            people[arr[i][2]] = 1

    if people[arr[i][2]] == 1 and people[arr[i][1]] == 0:
        if shake[arr[i][2]] < K:
            people[arr[i][1]] = 1

    shake[arr[i][1]] += 1
    shake[arr[i][2]] += 1

result = people[1:]
print(*result, sep='')