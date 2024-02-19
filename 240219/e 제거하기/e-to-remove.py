txt = input()
arr = list(txt)
for i in range(len(arr)):
    if arr[i] == 'e':
        arr.pop(i)
        break

print(''.join(arr), sep='')