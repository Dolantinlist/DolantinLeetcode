def quick_sort(nums, low=None, high=None):
    if not low and not high:
        low = 0
        high = len(nums) - 1
    if low >= high:
        return nums
    key = nums[low]
    i, j = low, high
    while(i < j):
        while(i < j and nums[j] >= key):
            j -= 1
        nums[i] = nums[j]
        while(i < j and nums[i] <= key):
            i += 1
        nums[j] = nums[i]
    nums[i] = key
    quick_sort(nums, low, i - 1)
    quick_sort(nums, i + 1, high)
    return nums

print(quick_sort([2,1,5,3,8,5,6]))