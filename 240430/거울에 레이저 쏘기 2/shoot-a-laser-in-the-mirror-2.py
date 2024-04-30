# N = int(input())
# arr = [list(input()) for _ in range(N)]
# K = int(input())
# # 아래 / 왼 / 위 / 오른
# dx, dy = [1,0,-1,0],[0,-1,0,1]
# cnt = 0

# if 1 <= K < N:
#     x = 0
#     y = K-1
#     d = 0
#     while 0<=x<N and 0<=y<N:
#         if arr[x][y] == '/':
#             d = (d + 1) % 4
#             x = x + dx[d]
#             y = y + dy[d]
#         else:
#             if d == 0:
#                 d = 3
#             elif d == 1:
#                 d = 2
#             elif d == 2:
#                 d = 1
#             elif d == 3:
#                 d = 0
            
#             x = x + dx[d]
#             y = y + dy[d]
#         cnt += 1
            

# elif N+1 <= K < 2*N:
#     x = K-N-1
#     y = N-1
#     d = 1
#     while 0<=x<N and 0<=y<N:
#         if arr[x][y] == '/':
#             d = (d + 1) % 4
#             x = x + dx[d]
#             y = y + dy[d]
#         else:
#             if d == 0:
#                 d = 3
#             elif d == 1:
#                 d = 2
#             elif d == 2:
#                 d = 1
#             elif d == 3:
#                 d = 0
            
#             x = x + dx[d]
#             y = y + dy[d]
#         cnt += 1

# elif 2*N+1 <= K < 3*N:
#     x = N-1
#     y = 3*N-K
#     d = 2
#     while 0<=x<N and 0<=y<N:
#         if arr[x][y] == '/':
#             d = (d + 1) % 4
#             x = x + dx[d]
#             y = y + dy[d]
#         else:
#             if d == 0:
#                 d = 3
#             elif d == 1:
#                 d = 2
#             elif d == 2:
#                 d = 1
#             elif d == 3:
#                 d = 0
            
#             x = x + dx[d]
#             y = y + dy[d]
#         cnt += 1

# else:
#     x = 4*N-K
#     y = 0
#     d = 3
#     while 0<=x<N and 0<=y<N:
#         if arr[x][y] == '/':
#             d = (d + 1) % 4
#             x = x + dx[d]
#             y = y + dy[d]
#         else:
#             if d == 0:
#                 d = 3
#             elif d == 1:
#                 d = 2
#             elif d == 2:
#                 d = 1
#             elif d == 3:
#                 d = 0
            
#             x = x + dx[d]
#             y = y + dy[d]
#         cnt += 1

# print(cnt)


# \
# 아래로 내려오면 오른쪽 방향으로 나감
# 왼쪽 방향으로 들어오면 위로 나감
# 오른쪽 방향으로 들어오면 아래로 나감
# 위쪽 방향으로 들어오면 왼쪽으로 나감
# 즉 아래 - 오른쪽 / 위 - 왼쪽 이렇게 묶을 수 있음

# /
# 아래 -> 왼
# 위 -> 오른
# 왼 -> 위
# 오른 -> 아래
# 시계방향으로 돈다

# K = 1 ~ N : (0,K-1)
# K = N+1~2N : (K-N-1, N-1)
# K = 2N+1~3N : (N-1, 3N-K)
# K = 3N+1~4N : (4N-K, 0)

def change_direction(current_direction, mirror):
    # 현재 방향이 위쪽인 경우
    if current_direction == 0:
        if mirror == '/':
            return 3  # 반시계방향으로 변경
        else:
            return 1  # 시계방향으로 변경
    
    # 현재 방향이 왼쪽인 경우
    elif current_direction == 1:
        if mirror == '/':
            return 0
        else:
            return 2
    
    # 현재 방향이 아래쪽인 경우
    elif current_direction == 2:
        if mirror == '/':
            return 1
        else:
            return 3
    
    # 현재 방향이 오른쪽인 경우
    elif current_direction == 3:
        if mirror == '/':
            return 2
        else:
            return 0

N = int(input())
arr = [list(input()) for _ in range(N)]
K = int(input())

# 아래 / 왼 / 위 / 오른
dx, dy = [1,0,-1,0], [0,-1,0,1]
cnt = 0

if 1 <= K < N:
    x = 0
    y = K-1
    d = 0
    while 0 <= x < N and 0 <= y < N:
        if arr[x][y] == '/':
            d = change_direction(d, '/')
        else:
            d = change_direction(d, '\\')
        
        x += dx[d]
        y += dy[d]
        cnt += 1

elif N+1 <= K < 2*N:
    x = K-N-1
    y = N-1
    d = 1
    while 0 <= x < N and 0 <= y < N:
        if arr[x][y] == '/':
            d = change_direction(d, '/')
        else:
            d = change_direction(d, '\\')
        
        x += dx[d]
        y += dy[d]
        cnt += 1

elif 2*N+1 <= K < 3*N:
    x = N-1
    y = 3*N-K
    d = 2
    while 0 <= x < N and 0 <= y < N:
        if arr[x][y] == '/':
            d = change_direction(d, '/')
        else:
            d = change_direction(d, '\\')
        
        x += dx[d]
        y += dy[d]
        cnt += 1

else:
    x = 4*N-K
    y = 0
    d = 3
    while 0 <= x < N and 0 <= y < N:
        if arr[x][y] == '/':
            d = change_direction(d, '/')
        else:
            d = change_direction(d, '\\')
        
        x += dx[d]
        y += dy[d]
        cnt += 1

print(cnt)