class Solution:
    def nextGreaterElement(self, nums1, nums2):
        tmp = {}
        l_stack = []
        rlt = []
        for x in nums2:
            while l_stack and l_stack[-1] < x:
                tmp[l_stack.pop()] = x
            l_stack.append(x)

        for x in nums1:
            rlt.append(tmp.get(x, -1))
        return rlt

print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))