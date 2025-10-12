class Solution:
    def subarrayBitwiseORs(self, arr):
        s = []    # Step 1: List to hold intermediate OR values
        l = 0     # Pointer to track new additions each round

        # Step 2: Loop through each element
        for a in arr:  
            r = len(s)  
            s.append(a)  

            # Step 3: OR current 'a' with all previous results from last round
            for i in range(l, r):
                v = s[i] | a
                
                # Step 3.1: Avoid adding duplicate value
                if v != s[-1]:  
                    s.append(v)

            # Step 4: Move l to the start of the current round's new values
            l = r

        # Step 5: Return the count of unique OR results
        return len(set(s)) 