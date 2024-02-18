txt, n = input().split()
n = int(n)
txt = list(txt)

for _ in range(n):
    arr = input().split()
    if arr[0] == '1':
        txt[int(arr[1])-1], txt[int(arr[2])-1] = txt[int(arr[2])-1], txt[int(arr[1])-1]
    
    if arr[0] == '2':
        for i in range(len(txt)):
            if txt[i] == arr[1]:
                txt[i] = arr[2]

    print(''.join(txt))