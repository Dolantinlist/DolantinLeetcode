
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s)==0:
            return 0
        hashmap={str(i):i for i in range(10)}
        ans=0
        flag=1
        if s[0] in hashmap:
            ans=hashmap[s[0]]
        elif s[0]=="+":
            pass
        elif s[0]=="-":
            flag=-1
        else:
            return 0
        for i in s[1:]:
            if i not in hashmap:
                return 0
            else:
                ans=ans*10+hashmap[i]
        return ans*flag

print(Solution().StrToInt("342"))