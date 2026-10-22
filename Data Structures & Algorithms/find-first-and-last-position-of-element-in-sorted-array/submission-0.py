class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def binary_search(is_left_search):
            left, right = 0, len(nums)-1
            res = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    res = mid
                    if is_left_search:
                        right = mid-1
                    else:
                        left = mid+1
            return res
        
        left = binary_search(True)
        right = binary_search(False)

        return [left, right]