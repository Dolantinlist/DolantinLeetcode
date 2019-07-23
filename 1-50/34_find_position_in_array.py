class Solution:
# @param A, a list of integers
# @param target, an integer to be searched
# @return a list of length 2, [index1, index2]
    def searchRange(self, arr, target):
        if not arr:
            return [-1, -1]
        start = self.binary_search(arr, target-0.5)
        if arr[start] != target:
            return [-1, -1]
        arr.append(0)
        end = self.binary_search(arr, target+0.5)-1
        return [start, end]

    def binary_search(self, arr, target):
        start, end = 0, len(arr)-1
        while start < end:
            mid = (start+end)//2
            if target < arr[mid]:
                end = mid
            else:
                start = mid+1
        return start


nums = [5,7,7,8,8,10]
target = 6
rlt = Solution().search_range(nums,target)
for i in rlt:
    print(i)