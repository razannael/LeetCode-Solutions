class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0 
        altitude = 0

        for x in gain: 
            altitude += x
            ans = max(ans, altitude)

        return ans