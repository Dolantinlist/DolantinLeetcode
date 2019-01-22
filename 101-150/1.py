import operator
def main():
    cnt = input()
    p = input()
    tokens = p.split()
    res = solve(tokens)
    return max(res)

def solve(tokens):
    res = []
    nums = map(int, tokens[::2])
    nums = list(nums)
    ops = map({'+': operator.add, '*': operator.mul}.get, tokens[1::2])
    ops = list(ops)
    def build(lo, hi):
        if lo == hi:
            return [nums[lo]]
        return [ops[i](a, b)
                for i in range(lo, hi)
                for a in build(lo, i)
                for b in build(i + 1, hi)]
    return build(0, len(nums) - 1)

if __name__ == '__main__':
    print(main())

