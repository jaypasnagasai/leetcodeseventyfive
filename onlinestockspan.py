#901. Online Stock Span

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        
        self.stack.append([price, ans])
        return ans
