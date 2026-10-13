class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        balance_map = collections.defaultdict(int)

        for payer, payee, amount in transactions:
            balance_map[payer] -= amount
            balance_map[payee] += amount
        
        balance = [amount for amount in balance_map.values() if amount]

        memo = {}

        def dfs(balance):

            if not balance:
                return 0
            
            index = tuple(balance)
            if index in memo:
                return memo[index]
            
            res = float('inf')
            for i in range(1, len(balance)):
                if balance[0] * balance[i] < 0:
                    new_balance = balance[1:i] + balance[i+1:]
                    if balance[0] + balance[i] != 0:
                        new_balance.append(balance[0] + balance[i])
                    res = min(res, 1 + dfs(sorted(new_balance)))
            
            memo[index] = res
            return res
        
        return dfs(sorted(balance))
                    