class Solution:
    # once you cast a spell, disable spells with value -2 to +2
    # this is like delete and earn.
    #   - de is -1 to +1: either cur + 2ago or 1ago
    #   - this is -2 to +2: either cur + 3ago or 1ago
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        strength = {k: k*count[k] for k in count}
        spells = [0, 0, 0] + sorted(list(strength.keys()))
        n = len(spells)
        dp = [0]*n
        for i in range(3, n):
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + strength[spells[i]]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strength[spells[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strength[spells[i]])
        
        return dp[-1]