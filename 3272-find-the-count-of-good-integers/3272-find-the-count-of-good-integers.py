class Solution(object):
    def __init__(self):
        self.res = 0
        self.visited = set()

    def vectorToNumber(self, digits):
        return int(''.join(map(str, digits)))

    def totalPermutations(self, freqMap, total):
        res = factorial(total)
        for count in freqMap.values():
            res //= factorial(count)
        return res

    def permsWithZero(self, freqMap, total):
        if freqMap.get(0, 0) == 0:
            return 0
        freqMap[0] -= 1
        res = factorial(total - 1)
        for count in freqMap.values():
            res //= factorial(count)
        return res

    def genPal(self, palin, left, right, divisor, total):
        if left > right:
            palinVal = self.vectorToNumber(palin)
            if palinVal % divisor == 0:
                freq = Counter(palin)
                key = tuple(sorted(freq.items()))
                if key not in self.visited:
                    self.res += self.totalPermutations(freq, total) - self.permsWithZero(freq.copy(), total)
                    self.visited.add(key)
            return

        for dig in range(1 if left == 0 else 0, 10):
            palin[left] = palin[right] = dig
            self.genPal(palin, left + 1, right - 1, divisor, total)

    def countGoodIntegers(self, n, k):
        self.res = 0
        self.visited.clear()
        self.genPal([0] * n, 0, n - 1, k, n)
        return self.res