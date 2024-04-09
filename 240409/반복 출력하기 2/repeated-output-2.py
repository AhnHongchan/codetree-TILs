n = int(input())

def say(n):
    if n == 0:
        return
    print('HelloWorld')
    say(n-1)

say(n)