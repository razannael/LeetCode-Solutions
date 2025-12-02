class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        counts = Counter(y for _, y in points).values()
        horizCnts = [comb(c,2) for c in counts]
        
        totalCnt = sum(horizCnts)
        squares = sum(map(mul, horizCnts, horizCnts))
        
        ans = (totalCnt * totalCnt//2) %1_000_000_007
        ans-= (squares//2) %1_000_000_007
    
        return ans %1_000_000_007