def generateParenthesis(n):
    def generate(p, left, right, paren = []):
        if left > 0:
            generate(p + '(', left - 1, right)
        if right > left:
            generate(p + ')', left, right - 1)
        if right == 0:
            paren.append(p)
        return paren
    return generate('', n, n)

print(generateParenthesis(3))