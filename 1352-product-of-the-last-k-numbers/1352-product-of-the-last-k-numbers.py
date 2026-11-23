class ProductOfNumbers:

    def __init__(self):
        self.product=[1]
        self.n=1

    def add(self, num: int) -> None:
        if num==0:
            self.product=[1]
            self.n=1
        else:
            self.product.append(self.product[-1]*num)
            self.n+=1

    def getProduct(self, k: int) -> int:
        if self.n<=k:
            return 0
        else:
            return self.product[-1]//self.product[-k-1]