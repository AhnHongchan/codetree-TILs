def calculate_counts(a, b):
    count1 = 0  # 1번 카운트
    count2 = 0  # 2번 카운트
    for i in range(3):
        if a[i] == b[i]:
            count1 += 1
        elif a[i] in b:
            count2 += 1
    return count1, count2

def is_possible_number(possible_num, queries):
    for query in queries:
        b = query[0]
        expected_count1 = query[1]
        expected_count2 = query[2]
        
        count1, count2 = calculate_counts(possible_num, b)
        if count1 != expected_count1 or count2 != expected_count2:
            return False
    return True

def find_possible_numbers(n, queries):
    from itertools import permutations
    
    all_possible_numbers = [''.join(p) for p in permutations('123456789', 3)]
    possible_numbers = []

    for num in all_possible_numbers:
        if is_possible_number(num, queries):
            possible_numbers.append(num)
    
    return len(possible_numbers)

# 입력 받기
n = int(input())
queries = []

for _ in range(n):
    b, count1, count2 = input().split()
    queries.append((b, int(count1), int(count2)))

# 가능한 숫자 찾기
result = find_possible_numbers(n, queries)
print(result)