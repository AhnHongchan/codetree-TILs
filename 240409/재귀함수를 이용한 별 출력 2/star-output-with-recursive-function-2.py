N = int(input())

def star_recur(N):
    if N == 0:
        return
    print('* ' * N)
    star_recur(N-1)
    print('* ' * N)

star_recur(N)