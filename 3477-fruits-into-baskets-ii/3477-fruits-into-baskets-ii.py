class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        n, ans = len(baskets), 0
        
        for fruit in fruits:
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    break

            else: ans += 1

        return ans