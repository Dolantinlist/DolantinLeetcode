class Solution(object):
    def jump2(self, A):
        ans = lastIdx = nextIdx = 0
        while nextIdx < len(A) - 1:
            ans += 1
            lastIdx, nextIdx = nextIdx, max(i + A[i] for i in range(lastIdx, nextIdx + 1))
        return ans
input = [1,3,2,4,3,4]
#input = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
print(Solution().jump2(input))


