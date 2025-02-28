class Solution:
    def countAndSay(self, n: int) -> str:
        pattern = "1"
        def compress(pattern):
            count = 1
            res = ""
            for i in range(1,len(pattern)):
                if pattern[i] == pattern[i-1]:
                    count += 1
                else:
                    res = res + str(count) + pattern[i-1]
                    count = 1
            res += str(count) + pattern[-1]
            return res
                

        for i in range(n-1):
            pattern = compress(pattern)
            #print(pattern)
        
        return pattern
        
        