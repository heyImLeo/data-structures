class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left<=right:
            mid = (left+right)//2
            sq = mid*mid
            if  sq == x:
                return mid
            if sq > x:
                right = mid-1
            else:
                left = mid+1
                res = mid
        
        return res
            