n = int(input())

def say(n):
    if n == 0:
        return
    say(n-1)
    print('HelloWorld')

say(n)