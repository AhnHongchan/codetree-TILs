from itertools import combinations

# 입력 받기
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

def is_non_overlapping(segment_list):
    # 주어진 선분 리스트가 겹치지 않는지 확인하는 함수
    segment_list.sort()  # 시작점을 기준으로 정렬
    for i in range(len(segment_list) - 1):
        if segment_list[i][1] >= segment_list[i + 1][0]:  # 끝점이 다음 선분의 시작점보다 크면 겹침
            return False
    return True

count = 0

# 모든 3개를 제거하는 조합에 대해 확인
for removed_segments in combinations(segments, 3):
    remaining_segments = [segment for segment in segments if segment not in removed_segments]
    if is_non_overlapping(remaining_segments):
        count += 1

print(count)