class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flippedK = 0
        left = 0
        maxWindow = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                flippedK += 1

            while flippedK > k:
                if nums[left] == 0:
                    flippedK -= 1
                left += 1

            maxWindow = max(maxWindow, right - left + 1)

        return maxWindow