class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a=[]
        sqrt=int(n**0.5)
        for i in range (1,sqrt+1):
            if n%i==0:
              a.append(i)
              if n//i!=i:
                a.append(n//i)
        a.sort()
        if len(a)>=k:
               return a[k-1]
        else:
               return -1