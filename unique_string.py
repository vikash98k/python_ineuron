from collections import Counter
def func(string):
    count = Counter(string)
    print(count)
    for key,value in count.items():
        if value == 1:
            return string.index(key)
            break
    return -1
string ="leetcode"
print(func(string))