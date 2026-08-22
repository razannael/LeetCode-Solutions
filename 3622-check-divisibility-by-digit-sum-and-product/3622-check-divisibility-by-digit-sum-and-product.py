class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_str=str(n)
        prod=1
        su=0
        for i in n_str:
            prod*=int(i)
            su+=int(i)   
        return n%(prod+su)==0    


        