class Solution:
    def duplicate(self, numbers, duplication):
        l = len(numbers)
        for i in range(len(numbers)):
            index = numbers[i]
            if index >= l:
                index -= l
            if numbers[index] >= l:
                return index
            numbers[index] += l
        return  -1

print(Solution().duplicate([2,3,1,0,2], 0))
