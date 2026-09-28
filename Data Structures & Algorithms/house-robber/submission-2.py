class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)-1
        def _rob(index):
            if index > n:
                return 0
            
            if index in memo:
                return memo[index]
            
            rob_start = nums[index] + _rob(index+2)
            rob_skip = _rob(index+1)
            memo[index] = max(rob_start, rob_skip)
            return memo[index]
        
        return _rob(0)