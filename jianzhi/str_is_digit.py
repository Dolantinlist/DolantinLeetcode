
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        a=['0','1','2','3','4','5','6','7','8','9']
        b=['+','-']
        c=['E','e']
        num_c,num_d,num_e=0,0,0
        if not s:
            return False
        for i in range(len(s)):
            if s[i] in b:
                num_c+=1        #符号计数，大于两个肯定错
                if i==0:#符号在开头，之后没东西错误，之后跟的不是数字或小数点错误
                    if (i+1>len(s)) or ((s[i+1] not in a) and (s[i+1]!='.')):
                        return False
                if i==1:#符号在第二位肯定错
                    return False
                if i>=2:#符号在第三位及之后(9e-1最早为第三位),符号之前只能是e
                    if (s[i-1] not in c):
                        return False
            if s[i] in c:
                num_e+=1        #e计数，大于一个错误
                if i+1>=len(s):     #e之后没东西错误
                    return False
                for j in s[i+1:]:   #e之后小数点错误
                    if j == '.':
                        return False
            if s[i] == '.':
                num_d+=1        #小数点计数，大于一个肯定错
                if (s[i+1] not in a) or ((s[i-1] not in a) and (s[i-1] not in b) and (i<1)):
                    #小数点前有东西时，若不是符号或数字就错误，小数点后不是数字错误
                    return False
            if num_e>1 or num_d>1 or num_c>2:   #计数判断错误
                return False
            if (s[i] not in a) and (s[i] not in b) and (s[i] not in c) and s[i]!='.':
                #出现不是数字小数点符号e的就错误
                return False
        return True #遍历完就正确