import math
class Solution(object):
    def getPermutation(self, n, k):
        permutation = ''
        numbers = list(range(1, n + 1))
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial())
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        return permutation