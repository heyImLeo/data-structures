class Solution:
    def climbStairs(self, n: int) -> int:
        def _run(n, memo):
            if n < 0:
                return 0
            
            if n == 0:
                return 1
            
            if n in memo:
                return memo[n]
            
            memo[n] = _run(n-1, memo) + _run(n-2, memo)
            return memo[n]
        
        return _run(n, {})
