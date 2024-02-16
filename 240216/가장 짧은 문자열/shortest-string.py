min_val = 100

for i in range(3):
    txt = input()
    length = len(txt)
    if min_val > length:
        min_val = length

print(min_val)