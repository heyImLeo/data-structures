class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq, trace = Counter(s1), {}
        left = 0

        for right in range(len(s2)):
            trace[s2[right]] = 1 + trace.get(s2[right], 0)
            while right - left + 1 > len(s1):
                trace[s2[left]] -= 1
                if trace[s2[left]] == 0:
                    del trace[s2[left]]
                left+=1
            
            if trace == freq:
                return True
        
        return False
            
