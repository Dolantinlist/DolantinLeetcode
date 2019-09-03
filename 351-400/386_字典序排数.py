'''
思路：能往后加0就往后加0
不能加0了就在最后一位的基础上加1 加到上限n后给n整除10
加到10的倍数后就不断给该数/10降级  例如1100->110->11  然后把11加到res中
循环重复上述过程
'''
class Solution:
    def lexicalOrder(self, n):
        res = []
        cur = 1
        for _ in range(n):
            res.append(cur)
            if cur*10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur%10 == 0:
                    cur //= 10
        return res

print(Solution().lexicalOrder(13))
