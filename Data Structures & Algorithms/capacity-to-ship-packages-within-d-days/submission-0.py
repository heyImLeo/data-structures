class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        while left<=right:
            mid = (left+right)//2

            totalDays = 1
            curSum = 0
            for weight in weights:
                if curSum + weight> mid:
                    totalDays+=1
                    curSum = weight
                else:
                    curSum += weight
            
            if totalDays <= days:
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res