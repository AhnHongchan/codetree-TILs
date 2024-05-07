arr = [list(map(int, input().split())) for _ in range(19)]
result = False

# 수직 방향 검사
for i in range(15):
    for j in range(19):  # 15까지만 검사해야 수직으로 5개가 될 수 있음
        a = arr[i][j]
        if a == 0:
            continue
        else:
            for k in range(1, 5):
                b = arr[i+k][j]
                if a != b:
                    break
            else:
                print(a)
                print(i+3, j+1)
                result = True
                break
    if result:
        break

if not result:  # 수직 방향으로 오목이 없는 경우에만 수평과 대각선 검사
    # 수평 방향 검사
    for i in range(19):  # 15까지만 검사해야 수평으로 5개가 될 수 있음
        for j in range(15):
            a = arr[i][j]
            if a == 0:
                continue
            else:
                for k in range(1, 5):
                    b = arr[i][j+k]
                    if a != b:
                        break
                else:
                    print(a)
                    print(i+1, j+3)
                    result = True
                    break
        if result:
            break

if not result:  # 수직, 수평 방향으로 오목이 없는 경우에만 대각선 검사
    # 대각선 방향 검사 (우상향 방향)
    for i in range(15):
        for j in range(15):
            a = arr[i][j]
            if a == 0:
                continue
            else:
                for k in range(1, 5):
                    b = arr[i+k][j+k]
                    if a != b:
                        break
                else:
                    print(a)
                    print(i+3, j+3)
                    result = True
                    break
        if result:
            break

if not result:  # 수직, 수평, 대각선 방향으로 오목이 없는 경우에만 대각선 검사 (우하향 방향)
    # 대각선 방향 검사 (우하향 방향)
    for i in range(15):  # 가로 인덱스 범위: 4 이상부터
        for j in range(4, 19):
            a = arr[i][j]
            if a == 0:
                continue
            else:
                for k in range(1, 5):
                    b = arr[i-k][j+k]
                    if a != b:
                        break
                else:
                    print(a)
                    print(i+3, j-1)
                    result = True
                    break
        if result:
            break