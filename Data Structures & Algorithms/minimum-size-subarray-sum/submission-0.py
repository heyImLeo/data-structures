class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum, left = 0, 0
        res = float('inf')

        for right in range(len(nums)):
            curSum += nums[right]
            while curSum >= target:
                res = min(res, right-left+1)
                curSum -= nums[left]
                left+=1
        return res if res !=float('inf') else 0