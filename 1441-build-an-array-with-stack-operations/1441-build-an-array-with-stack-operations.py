class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        i = 1
        j = 1
        new = []

        while i < len(target)+1:
            if target[i-1] == j:
                new.append('Push')
                i += 1
            else:
                new.append('Push')
                new.append('Pop')

            
            j += 1
        
        return new