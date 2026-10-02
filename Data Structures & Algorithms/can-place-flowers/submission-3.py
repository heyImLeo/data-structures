class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        f = [0] + flowerbed + [0]
        if n == 0:
            return True

        for i in range(1, len(f) - 1):
            if f[i] == 0 and f[i-1] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        
        return n <= 0
         