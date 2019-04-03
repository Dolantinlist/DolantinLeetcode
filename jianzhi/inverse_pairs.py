class Solution:
    def InversePairs(self, data):
        rlt = self.mergeHelper(data, 0, len(data)-1)
        return rlt%1000000007

    def mergeHelper(self, array, start, end):
        if start >= end:
            return 0

        mid = int((start + end)/2)
        leftcnt = self.mergeHelper(array, start, mid)
        rightcnt = self.mergeHelper(array, mid + 1, end)

        copy = array[:]
        cnt = 0
        leftp, rightp, copyp = mid, end, end
        while leftp >= start and rightp >= mid + 1:
            if array[leftp] > array[rightp]:
                cnt += rightp - mid
                copy[copyp] = array[leftp]
                leftp -= 1
                copyp -= 1
            else:
                copy[copyp] = array[rightp]
                rightp -= 1
                copyp -= 1
        while leftp >= start:
            copy[copyp] = array[leftp]
            leftp -= 1
            copyp -= 1
        while rightp >= mid + 1:
            copy[copyp] = array[rightp]
            rightp -= 1
            copyp -= 1

        array[start:end+1] = copy[start:end+1]
        return cnt + leftcnt + rightcnt

t = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
print(Solution().InversePairs(t))