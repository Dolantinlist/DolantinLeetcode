class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        elif target == 0:
            flag = True
            for j in range(len(res)):
                if res[j] == path:
                    flag = False
            if flag:
                res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i+1, path + [nums[i]], res)