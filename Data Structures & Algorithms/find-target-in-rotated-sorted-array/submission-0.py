class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min_index():
            left, right = 0, len(nums)-1

            while left<right:
                mid = (left+right)//2
                if nums[mid] >= nums[right]:
                    left = mid+1
                else:
                    right = mid
            
            return left
        
        def binary_search(start, end, target):
            left, right = start, end
            while left<=right:
                mid=(left+right)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left=mid+1
                else:
                    right=mid-1
            return -1

        
        min_index = find_min_index()
        left_search = binary_search(0, min_index-1, target)
        right_search = binary_search(min_index, len(nums)-1, target)
        
        if left_search == -1:
            return right_search
        
        return left_search