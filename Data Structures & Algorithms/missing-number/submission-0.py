class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        total = set(nums)
        while True:
            if i not in total:
                return i
            i+=1
        