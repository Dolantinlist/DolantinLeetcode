class Solution:
    def decodeString(self, s):
        curstring, curnum = "", 0
        stack = []
        for c in s:
            if c == '[':
                stack.append(curnum)
                stack.append(curstring)
                curstring = ''
                curnum = 0
            elif c == ']':
                curstring = stack.pop() + stack.pop() * curstring
                curnum =  0
            elif c.isdigit():
                curnum = 10*curnum + int(c)
            else:
                curstring += c
        return curstring

print(Solution().decodeString("2[abc]3[cd]ef"))