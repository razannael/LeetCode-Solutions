class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        num=[abs(x) for x in nums]
        num.sort()
        n=len(num)
        i=n-1
        j=n-2
        ans=0
        while i>=0:
            while j>=0 and num[i] <= 2 * num[j]:
                j-=1
            ans+=i-j-1
            i-=1
        return ans
