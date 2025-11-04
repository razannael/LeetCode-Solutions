
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        pos = 0
        heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[pos]:
                pos += 1
            r = min(house - heaters[pos - 1], heaters[pos] - house)
            ans = max(ans, r)
        return ans