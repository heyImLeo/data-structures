class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum ,maxSum = 0, nums[0]

        for num in nums:
            curSum += num
            maxSum = max(maxSum, curSum)
            curSum = max(curSum, 0)
        return maxSum