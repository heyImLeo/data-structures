class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def _change(amount, coins, index, memo):
            key = (amount, index)

            if key in memo:
                return memo[key]

            if amount == 0:
                return 1
            
            if index > len(coins)-1:
                return 0
            
            total = 0
            coin = coins[index]

            for qty in range((amount//coin)+1):
                remainder = amount - (qty*coin)
                total += _change(remainder, coins, index+1, memo)
            
            memo[(amount, index)] = total
            return memo[(amount, index)]
    
        return _change(amount, coins, 0, memo)