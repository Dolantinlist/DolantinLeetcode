class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for i in preorder.split(','):
            stack+=[i]
            while stack[-2:] == ['#','#'] and len(stack)>2 and stack[-3]!='#':
                stack=stack[:-3]+['#']
        return stack == ['#']

print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))