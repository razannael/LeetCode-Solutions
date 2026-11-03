class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(n-1):
            temp=one+two
            one=two
            two=temp
        return two
    #please upvote me it would encourage me alot
