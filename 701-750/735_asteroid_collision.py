class Solution(object):
    def asteroidCollision(self, asteroids):
        rlt = []
        if not asteroids:
            return rlt
        i = 0
        cur = asteroids[i]
        stack = []
        while True:
            next = True
            if cur > 0:
                stack.append(cur)

            else:
                if not stack:
                    rlt.append(cur)
                else:
                    tmp = stack[-1]
                    if abs(cur) > tmp:
                        stack.pop()
                        next = False
                    elif abs(cur) == tmp:
                        stack.pop()

            if next:
                i += 1
                if i < len(asteroids):
                    cur = asteroids[i]
                else:
                    break
        rlt.extend(stack)
        return rlt

asteroids = [-2, -1, 1, 2]
print(Solution().asteroidCollision(asteroids))