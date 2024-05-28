def get_nearby_numbers(n, num):
    return [(num + i - 1) % n + 1 for i in range(-2, 3)]

def get_all_combinations(n, a, b, c):
    combinations = set()
    for i in get_nearby_numbers(n, a):
        for j in get_nearby_numbers(n, b):
            for k in get_nearby_numbers(n, c):
                combinations.add((i, j, k))
    return combinations

n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

combinations1 = get_all_combinations(n, a1, b1, c1)
combinations2 = get_all_combinations(n, a2, b2, c2)

all_combinations = combinations1.union(combinations2)

print(len(all_combinations))