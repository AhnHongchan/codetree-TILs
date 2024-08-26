def get_max_distance(seats):
    max_distance = 0

    for i in range(len(seats)):
        if seats[i] == '0':  # 빈 자리만 고려
            seats[i] = '1'  # 사람을 이 자리에 앉힌다
            
            # 거리 계산
            last_person = -1
            min_distance = len(seats)  # 현재 가능한 최소 거리를 최대값으로 초기화
            for j in range(len(seats)):
                if seats[j] == '1':
                    if last_person != -1:
                        min_distance = min(min_distance, j - last_person)
                    last_person = j

            max_distance = max(max_distance, min_distance)  # 최대 최소 거리를 업데이트

            seats[i] = 0  # 원래 상태로 복구

    return max_distance

n = int(input())
seats = list(input())

result = get_max_distance(seats)
print(result)