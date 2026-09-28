class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def _coin(amount):
            if amount < 0:
                return float('inf')
            
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            min_value = float("inf")
            for coin in coins:
                val = 1 + _coin(amount-coin)
                if val < min_value:
                    min_value = val
            memo[amount] = min_value
            print(memo[amount])
            return memo[amount]
        ans = _coin(amount)
        return ans if ans != float("inf") else -1