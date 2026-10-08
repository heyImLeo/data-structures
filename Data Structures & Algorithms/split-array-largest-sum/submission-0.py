class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def possible(val):
            pos = 1
            curSum = 0
            for num in nums:
                if (curSum + num) > val:
                    pos+=1
                    curSum = num
                else:
                    curSum += num
                
                if pos > k:
                    return False
            
            return pos <= k
        
        ans = 0
        low, high = max(nums), sum(nums)
        while low<=high:
            mid = (low+high)//2
            if possible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans