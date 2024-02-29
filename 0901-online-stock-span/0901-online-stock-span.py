class StockSpanner:

    def __init__(self):
        self.spans = []
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and price >= self.prices[-1]:
            span += self.spans.pop()
            self.prices.pop()
        self.prices.append(price)
        self.spans.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)