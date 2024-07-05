def diff_numbers(numbers):
    m = len(numbers)
    min_diff = 10000000

    # 모든 원소를 2배로 만들고
    for i in range(n):
        modified_numbers = numbers[:]
        modified_numbers[i] *= 2

        # 모든 원소를 제거하는 경우
        for j in range(n):
            if i == j:
                continue
            else:
                # 원소 제거된 리스트
                temp_numbers = modified_numbers[:j] + modified_numbers[j+1:]

                diff_sum = sum(abs(temp_numbers[k] - temp_numbers[k+1]) for k in range(n-2))

            min_diff = min(min_diff, diff_sum)
    return min_diff

n = int(input())
numbers = list(map(int, input().split()))
print(diff_numbers(numbers))