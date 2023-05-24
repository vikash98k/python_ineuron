
dictionary = {}
answer = []
target = 9
nums = [2, 7, 11, 15]
for i in range(len(nums)):
    secondNumber = target-nums[i]
    if(secondNumber in dictionary.keys()):
        secondIndex = nums.index(secondNumber)
        if(i != secondIndex):
            print(sorted([i, secondIndex]))
    dictionary.update({nums[i]: i})
    print(dictionary)