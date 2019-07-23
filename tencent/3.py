import sys

def find_min(nums, k):
    nums.sort()
    sum = 0
    i = 0
    while k:
        if i >= len(nums):
            print(0)
            k -= 1
        elif(nums[i] - sum) != 0:
            k -= 1
            print(nums[i] - sum)
            sum = nums[i]
        else:
            i += 1

if __name__ == '__main__':
    tmp = sys.stdin.readline().split()
    n = int(tmp[0])
    k = int(tmp[1])
    nums = list(map(int, sys.stdin.readline().split()))
    find_min(nums, k)