class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_count = 1
        for flower in flowerbed:
            if flower:
                empty_count = 0
            else:
                if empty_count == 2:
                    n -= 1
                    empty_count = 1
                else:
                    empty_count += 1
            if not n:
                return True
        return (n - (empty_count == 2)) == 0