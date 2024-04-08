def two(string):
    a = string[0]
    for i in range(1, len(string)):
        if string[i] != a:
            return 'Yes'
    return 'No'

string = input()
print(two(string))