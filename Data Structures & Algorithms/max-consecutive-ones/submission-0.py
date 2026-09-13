class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        res = 0

        for right in range(len(nums)):
            if nums[right]:
                res = max(res, right-left+1)
            else:
                left = right+1
        return res