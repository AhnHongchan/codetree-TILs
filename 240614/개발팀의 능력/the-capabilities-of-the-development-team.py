import itertools

def find_min_difference(abilities):
    # 모든 가능한 조합을 확인하기 위한 리스트 초기화
    min_difference = float('inf')
    
    # 5명의 능력치를 2명, 2명, 1명으로 나누는 모든 경우의 수를 구합니다.
    for team1 in itertools.combinations(abilities, 2):
        remaining1 = [x for x in abilities if x not in team1]
        for team2 in itertools.combinations(remaining1, 2):
            remaining2 = [x for x in remaining1 if x not in team2]
            team3 = remaining2
            
            # 각 팀의 능력치를 계산합니다.
            team1_sum = sum(team1)
            team2_sum = sum(team2)
            team3_sum = sum(team3)
            
            # 각 팀의 능력치가 모두 다르면
            if team1_sum != team2_sum and team2_sum != team3_sum and team1_sum != team3_sum:
                # 최대 능력치와 최소 능력치의 차이를 계산하여 최소 차이를 업데이트 합니다.
                max_ability = max(team1_sum, team2_sum, team3_sum)
                min_ability = min(team1_sum, team2_sum, team3_sum)
                difference = max_ability - min_ability
                min_difference = min(min_difference, difference)
    
    # 가능한 경우가 없다면 -1을 출력합니다.
    if min_difference == float('inf'):
        return -1
    else:
        return min_difference

# 입력 받기
abilities = list(map(int, input().split()))

# 결과 출력
print(find_min_difference(abilities))