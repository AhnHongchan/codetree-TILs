N = int(input())

def recur(N):
    if N == 0:
        return
    print(N, end=" ")
    recur(N-1)
    print(N, end=" ")

recur(N)