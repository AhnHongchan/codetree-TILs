a, b, c = map(int, input().split())
lst = [a, b, c]
lst.sort()
if len(lst) % 2 == 1:
    print(lst[(len(lst)-1) // 2])