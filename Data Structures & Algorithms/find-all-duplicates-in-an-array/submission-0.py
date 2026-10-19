class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        left = 0
        res = set()
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left = right
            else:
                res.add(nums[left])
        
        return list(res)
