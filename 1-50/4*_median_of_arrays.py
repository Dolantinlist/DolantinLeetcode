#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l%2:
            return self.find_kth(nums1, nums2, l//2)
        else:
            return (self.find_kth(nums1, nums2, l//2 - 1) + self.find_kth(nums1, nums2, l//2))/2

    def find_kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a)//2, len(b)//2
        ma, mb = a[ia], b[ib]
        if ia + ib < k:
            if ma > mb:
                return self.find_kth(a, b[ib+1:], k - ib - 1)
            else:
                return self.find_kth(a[ia+1:], b, k - ia - 1)
        else:
            if ma > mb:
                return self.find_kth(a[:ia], b, k)
            else:
                return self.find_kth(a, b[:ib], k)

print(Solution().findMedianSortedArrays([1,2], [3,4]))