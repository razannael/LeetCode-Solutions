class Solution(object):
    def gcd(self,a,b):
            if a == 0:
                return b
            return self.gcd(b % a, a)
    def lcm(self,a,b):
        return (a / self.gcd(a,b))* b
    def mirrorReflection(self, p,q):
        
        lcm=self.lcm(p,q)
        m=lcm//p
        n=lcm//q
        if n%2==0:
            return 2
        if m%2==0:
            return 0
        return 1
    
    
# basically you can just ignore the north wall and imagine the mirrors 
# as two parallel mirrors with just extending east and west walls and the end points of east walls are made of 0 reflector then 1 reflector the oth the 1th and so onn....
# eventually we gotta find the point where m*p=n*q
# and we can find m and n by lcm of p and q 
# now the consept is simple .....
# if number of extensions of q(ie n) is even that means the end reflection must have happened on west wall ie. reflector 2 else 
# else there are two possibility reflector 1 or 0 which depends on the value of m(ie. the full fledged square extentions) if its even or odd