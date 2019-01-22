from itertools import groupby
class Solution(object):
    def count_and_say(self, n):
        result = '1'
        for i in range(n - 1):
            tmp = ''
            for digit, group in groupby(result):
                tmp = tmp + (str(len(list(group)))) + digit
            result = tmp
        return result