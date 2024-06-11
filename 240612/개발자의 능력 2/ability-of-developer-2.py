from itertools import combinations

def minimize_team_difference(abilities):
    # 모든 가능한 2명 조합을 구합니다.
    all_pairs = list(combinations(range(6), 2))
    min_diff = float('inf')

    # 모든 가능한 3팀의 조합을 고려합니다.
    for team1 in all_pairs:
        remaining = set(range(6)) - set(team1)
        remaining = list(remaining)
        
        for team2 in combinations(remaining, 2):
            team3 = list(set(remaining) - set(team2))
            
            # 각 팀의 능력 합을 구합니다.
            sum1 = abilities[team1[0]] + abilities[team1[1]]
            sum2 = abilities[team2[0]] + abilities[team2[1]]
            sum3 = abilities[team3[0]] + abilities[team3[1]]
            
            # 최대와 최소 팀의 차이를 계산합니다.
            max_sum = max(sum1, sum2, sum3)
            min_sum = min(sum1, sum2, sum3)
            diff = max_sum - min_sum
            
            # 차이가 최소인 경우를 찾습니다.
            if diff < min_diff:
                min_diff = diff
    
    return min_diff

# 예제 입력
abilities = list(map(int, input().split()))
# 차이를 출력
print(minimize_team_difference(abilities))