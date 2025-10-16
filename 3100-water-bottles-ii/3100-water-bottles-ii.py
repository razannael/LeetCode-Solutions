class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        b = 2 * numExchange - 3
        c = 2 * (numBottles - 1)
        n = (-b + (b**2+4*c)**(1/2)) / 2  

        return numBottles + floor(n)
            

        