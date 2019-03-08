class Solution:
    def fizzBuzz(self, n):
        rlt = [""] *n
        for i in range(n):
            if (i+1) % 3 == 0:
                rlt[i] += "Fizz"
            if (i+1) % 5 == 0:
                rlt[i] += "Buzz"
            if len(rlt[i]) == 0:
                rlt[i] += str(i + 1)
        return rlt
