string = "AABC"
n = len(string)
if string == string[::-1]:
    print(0)
else:
    string = string[0:n-1]+string[::-1]
    print(string)