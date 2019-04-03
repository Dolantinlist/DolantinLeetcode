def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(a, b):
    rlt = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            rlt.append(a[i])
            i += 1
        else:
            rlt.append(b[j])
            j += 1
    if i == len(a):
        rlt.extend(b[j:])
    else:
        rlt.extend(a[i:])
    return rlt

print(merge_sort([2,5,1,3,8,4,3]))