from Tree import *
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        mid  = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


a = [-10,-3,0,5,9]
root = Solution().sortedArrayToBST(a)
print(levelOrder(root))