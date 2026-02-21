def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            c=0
            n=bin(i).count("1")
            for j in range(1,n+1):
                if n%j==0:
                    c+=1
            if c==2:
                count+=1
        return count