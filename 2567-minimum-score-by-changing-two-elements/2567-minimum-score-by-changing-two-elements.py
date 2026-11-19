class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        nums.sort()

        return min(nums[-1] - nums[2],  #  [a,b,c, ..., x,y,z] => [c,c,c, ..., x,y,z]
                   nums[-2] - nums[1],  #  [a,b,c, ..., x,y,z] => [b,b,c, ..., x,y,y] 
                   nums[-3] - nums[0])  #  [a,b,c, ..., x,y,z] => [a,b,c, ..., x,x,x]

                                        #  Return  min((z-c)+(c-c), (x-a)+(x-x), (y-b)+(b-b))