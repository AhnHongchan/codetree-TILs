def palindrome(string, n):
    for i in range(n//2):
        if string[i] == string[n-i-1]:
            continue
        else:
            return 'No'
    return 'Yes'

string = input()
n = len(string)
result = palindrome(string, n)
print(result)