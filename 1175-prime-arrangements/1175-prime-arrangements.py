class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime=[True]*(n+1)
        prime[0]=prime[1]=False
        for i in range(2,int(n**0.5)+1):
            if prime[i]==True:
                for j in range(i*i,n+1,i):
                    prime[j]=False
                    
        p=sum(prime)
        fact=[1]*(n+1)
        for i in range(1,n+1):
            fact[i]=fact[i-1]*i%(10**9+7)
        return (fact[p]*fact[n-p])%(10**9+7)

        