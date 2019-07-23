class Solution(object):
    def longest_valid_parenthese(self,s):
        stack = [0]
        result = 0
        for char in s:
            if char == '(':
                stack.append(0)
            elif len(stack) > 1:
                val = stack.pop()
                stack[-1] += val + 2
                result = max(result, stack[-1])
            else:
                stack = [0]
        return result

s = ")())(())"
print(Solution().longest_valid_parenthese(s))