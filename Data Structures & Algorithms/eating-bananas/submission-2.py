class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left<=right:
            mid = (left+right)//2
            time = 0
            for pile in piles:
                time+=math.ceil(pile/mid)
            
            if time<=h:
                res = mid
                right = mid-1
            else:
                left = mid+1
        
        return res
