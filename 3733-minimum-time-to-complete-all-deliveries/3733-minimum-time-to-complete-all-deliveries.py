class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        low = d[0] + d[1]
        high = 2 * (low) * 2 
        ans = high

        lcm = (r[0] * r[1]) // math.gcd(r[0], r[1])

        def can_complete(time):
            """
            Checks if all deliveries can be completed within 'time'
            by verifying all three capacity conditions.
            """
            # 1. Check Drone 1 capacity
            slots1 = time - (time // r[0])
            
            # 2. Check Drone 2 capacity
            slots2 = time - (time // r[1])
            
            # 3. Check total system capacity (accounting for shared recharge times)
            total_slots = time - (time // lcm)
            
            return (slots1 >= d[0]) and (slots2 >= d[1]) and (total_slots >= d[0] + d[1])

        # Binary search for the minimum time
        while low <= high:
            mid = (low + high) // 2
            if can_complete(mid):
                ans = mid       # This time works, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1   # This time doesn't work, need more time
        
        return ans