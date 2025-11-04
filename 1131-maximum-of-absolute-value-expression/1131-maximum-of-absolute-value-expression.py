class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        |a1[i]-a1[j]| + |a2[i]-a2[j]| + |i-j|
        total 2(+ or -)**(no. of modules) == 2**3 cases

        --> a1[i]-a1[j]+a2[i]-a2[j]+i-j
            == (a1[i]+a2[i]+i) - (a1[j]+a2[j]+j)

        --> a1[i]-a1[j]+a2[i]-a2[j]-i-j
            == (a1[i]+a2[i]-i) - (a1[j]+a2[j]-j)
        
        ...etc
        '''
        val1,val2,val3,val4=[],[],[],[]
        for i in range(len(arr1)):
            val1.append(i+arr1[i]+arr2[i])
            val2.append(i+arr1[i]-arr2[i])
            val3.append(i-arr1[i]+arr2[i])
            val4.append(i-arr1[i]-arr2[i])
        ans=0
        ans=max(ans,max(val1)-min(val1))
        ans=max(ans,max(val2)-min(val2))
        ans=max(ans,max(val3)-min(val3))
        ans=max(ans,max(val4)-min(val4))
        return ans