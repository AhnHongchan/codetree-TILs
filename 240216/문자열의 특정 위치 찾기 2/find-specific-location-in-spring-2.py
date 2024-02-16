arr = ["apple", "banana", "grape", "blueberry", "orange"]
string = input()
cnt = 0

for i in range(5):
    if arr[i][2] == string or arr[i][3] == string:
        cnt += 1
        print(arr[i])

print(cnt)