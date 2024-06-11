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

# 1. 먼저 제시된 조건들을 받아서 queries에 넣는다.
# 2. 가능한 숫자의 개수를 받아온다. 방법은 다음과 같다.
# 3. 먼저 순열을 이용해 숫자를 받아온다.
#   해설에서는 for문을 돌려서 111~999까지 확인했다.
# 4. 이 중에 가능한 숫자를 찾는다.
# 5. 가능한 숫자를 possible_numbers에 넣는다.
# 6. 먼저 숫자마다 다음과 같은 과정을 거친다
# 7. queries에 들어간 경우마다 비교해준다.
# 8. 실제 알려준 정보와 카운트했을 때 나오는 정보와 비교해서
# 가능한 숫지인지 확인한 후 가능하면 possible_numbers에 넣는다.
# 9. 이 과정을 모든 숫자에서 진행한다.