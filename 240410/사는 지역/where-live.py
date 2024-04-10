class Info:
    def __init__(self, name, post, address):
        self.name = name
        self.post = post
        self.address = address

n = int(input())
lst = []
for _ in range(n):
    name, post, address = input().split()
    lst.append([name, post, address])

lst.sort(key = lambda x:x[0])
a = lst.pop()
print(f'name {a[0]}')
print(f'addr {a[1]}')
print(f'city {a[2]}')