math_a, eng_a = map(int, input().split())
math_b, eng_b = map(int, input().split())

if math_a > math_b:
    print('A')
elif math_a < math_b:
    print('B')
elif math_a == math_b:
    if eng_a > eng_b:
        print('A')
    elif eng_a < eng_b:
        print('B')
    else:
        pass