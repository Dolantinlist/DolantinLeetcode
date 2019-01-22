class Solution(object):
    def simplifyPath(self, path):
        places = []
        for w in path.split("/"):
            if w != "." and w != "":
                places += [w]

        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)


print(Solution().simplifyPath("/home//foo/"))