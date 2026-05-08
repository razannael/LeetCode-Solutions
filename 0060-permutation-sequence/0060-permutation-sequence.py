def factorial(n):
    if n == 0 : return 1
    return n*factorial(n-1)

def get_sequence(n,k):
    seq = []
    k = k - 1
    for i in range(n-1,0,-1):
        quotient,remainder = k//factorial(i),k%factorial(i)
        seq.append(quotient)
        k = remainder
    return seq

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        sequene = get_sequence(n,k)
        res = ''
        array = [str(i) for i in range(1,n+1)]
        while sequene :
            index = sequene.pop(0)
            res +=array[index]
            del array[index]
        res +=array[0]
        return res 
        