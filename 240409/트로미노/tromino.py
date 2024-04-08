def stick():
    max_v = 0
    for i in range(n):    
        for j in range(m-2):
            sum_v = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            if max_v < sum_v:
                max_v = sum_v
    
    for j in range(m):
        for i in range(n-2):
            sum_v = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            if max_v < sum_v:
                max_v = sum_v
    
    return max_v

def square_blank():
    max_v2 = 0
    for i in range(n-1):
        for j in range(m-1):
            min_v = min(arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1])
            sum_v2 = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1] - min_v
            if max_v2 < sum_v2:
                max_v2 = sum_v2
    return max_v2

n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = max(stick(), square_blank())
print(result)