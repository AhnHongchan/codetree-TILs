num_list = list(map(int, input().split()))

new_list = []
for i in range(len(num_list)):
    if num_list[i] != 0:
        new_list.append(num_list[i])
    else:
        break

print(*new_list[::-1])