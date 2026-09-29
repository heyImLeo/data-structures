class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        totalNoGrumpy = 0

        for i in range(n):
            if not grumpy[i]:
                totalNoGrumpy+=customers[i]
        
        maxTotal, curSum = totalNoGrumpy, totalNoGrumpy
        
        left = 0
        for right in range(n):
            if grumpy[right]:
                curSum += customers[right]
            while right-left+1>minutes:
                if grumpy[left]:
                    curSum -= customers[left]
                left+=1
            
            if right-left+1==minutes:
                maxTotal = max(maxTotal, curSum)
        return maxTotal

                


