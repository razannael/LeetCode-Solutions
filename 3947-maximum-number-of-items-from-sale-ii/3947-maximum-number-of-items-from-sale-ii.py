class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        items.sort(key=lambda x: x[1])
        mx = max(factor for factor, _ in items)
        freq = [0] * (mx + 1)
        for factor, _ in items:
            freq[factor] += 1
        for i in range(1, mx + 1):
            if freq[i] > 0:
                for j in range(i * 2, mx + 1, i):
                    freq[i] += freq[j]

        mn = items[0][1]
        ans = 0
        for factor, price in items:
            if price > mn * 2:
                break
            cnt = freq[factor] - 1
            take = min(cnt, budget // price)
            ans += take * 2
            budget -= take * price
        ans += budget // mn
        return ans