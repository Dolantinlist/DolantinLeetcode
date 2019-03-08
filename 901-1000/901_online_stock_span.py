class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        print(res)

S = StockSpanner()
S.next(100)
S.next(80)
S.next(60)
S.next(70)
S.next(60)
S.next(75)
S.next(85)