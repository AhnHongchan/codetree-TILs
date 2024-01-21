math_a, eng_a = map(int, input().split())
math_b, eng_b = map(int, input().split())
print(int(math_a > math_b and eng_a > eng_b))