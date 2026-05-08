class Solution:
    def closestPrimes(self, l: int, r: int) -> List[int]:
        ans=[]
        def prime(i):
            if i<2:
                return False
            if i in (2,3,5):
                return True
            if i%2==0 or i%3==0 or i%5==0:
                return False
            for j in range(7,int(math.sqrt(i))+1,2):
                if i%j==0:
                    return False
            return True

        for i in range(l,r+1):
            if prime(i):
                ans.append(i)
            
        if len(ans)<2:
            return [-1,-1]
        val=float('inf')
        res=[0,0]
        for i in range(len(ans)-1):
            if ans[i+1]-ans[i]<val:
                res[0]=ans[i]
                res[1]=ans[i+1]
                val=ans[i+1]-ans[i]
        return res