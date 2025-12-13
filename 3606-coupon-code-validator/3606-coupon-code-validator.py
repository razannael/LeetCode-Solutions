class Solution:
    
    def validateCoupons(self, code: List[str], businessLine: List[str],
                              isActive: List[bool]) -> List[str]:
        ans = []
        d = defaultdict(int, {"electronics": 1, "grocery":2,    # <-- 1)  
                              "pharmacy":3, "restaurant":4})    #
                                                               
        data = list(zip(code, businessLine, isActive))          # <-- 2)   
        data.sort(key = lambda x:(d[x[1]], x[0]))               #
                        
        for coupId, busCat, curAct in data:                     #
            if not coupId.replace('_', 'a').isalnum(): continue # <-- 3)
            if d[busCat] == 0: continue                         #
            if not curAct: continue                             #    

            ans.append(coupId)

        return ans                                              # <-- 4)