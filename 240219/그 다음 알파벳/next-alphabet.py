char = input()
new = ord(char) + 1
if new >= 126:
    new -= 26

else:
    print(chr(new))