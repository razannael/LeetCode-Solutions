class Solution:
    def pathSum(self, nums: List[int]) -> int:
        mp =  collections.defaultdict()

        for n in nums:
            s = str(n)
            mp[(int(s[0]), int(s[1])-1)] = int(s[2])
    
        res = []    
        def helper(level , pos  , path):
            #edge condition checker
            if (level , pos) not in mp:
                return
    
            path+=mp[(level ,pos)]
    
            #check if its a leaf node (its level should) Logic to check for node is a leaf or nor
            if (level+1 , 2*pos) not in mp and (level+1 , 2*pos+1) not in mp:
                res.append(path)
                return
    
            helper(level+1   , 2*pos , path)
            helper(level+1 , 2*pos+1 , path)
    
    
            path-=mp[(level ,pos)]


        helper(1 , 0 ,0)

        return(sum(res))    