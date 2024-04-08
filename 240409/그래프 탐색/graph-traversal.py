# 노드 수, 간선 수
n, m = map(int, input().split())  

# 인접 리스트
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())

    # 양방향이므로 서로 넣어준다.
    graph[x].append(y)
    graph[y].append(x)

# 방문 리스트
visited = [False for _ in range(n + 1)]

def dfs(v):
    global cnt
    for i in graph[v]:
        if not visited[i]:
            # 1번 정점은 제외
            if i != 1:
                cnt += 1
            visited[i] = True
            dfs(i)

cnt = 0
dfs(1)
print(cnt)